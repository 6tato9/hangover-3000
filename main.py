import sys
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QListWidgetItem
from app import Ui_MainWindow
from database import HangoverDatabase

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.db = HangoverDatabase()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.add.clicked.connect(self.add_record)
        self.ui.update.clicked.connect(self.update_record)
        self.ui.delete_2.clicked.connect(self.delete_record)

        self.ui.listWidget.currentItemChanged.connect(self.load_selected_record)

        self.selected_id = None
        self.refresh_records()
        self.clear_inputs()

    def add_record(self):
        date = self.ui.whendata.date().toString("yyyy-MM-dd")
        name = self.ui.name.text().strip()
        glasses = self.ui.glasses.value()
        severity = self.ui.rate.value()
        story = self.ui.story.toPlainText().strip()

        if not name:
            QMessageBox.warning(self, "შეცდომა", "შეიყვანე სასმელის სახელი.")
            return
        if glasses == 0:
            QMessageBox.warning(self, "შეცდომა", "მიუთითე რამდენი ჭიქა დალიე.")
            return

        self.db.insert(date, name, glasses, severity, story)
        QMessageBox.information(self, "დამატება", "✅ ჩანაწერი წარმატებით დაემატა!")
        self.refresh_records()
        self.clear_inputs()

    def refresh_records(self):
        self.ui.listWidget.clear()
        cursor = self.db.conn.cursor()
        cursor.execute("SELECT id, date, drink_name, glasses FROM drinks ORDER BY id DESC")
        records = cursor.fetchall()

        for rec in records:
            rec_id, date, drink, glasses = rec
            item_text = f"{date} - {drink} - {glasses} ჭიქა"
            item = QListWidgetItem(item_text)
            item.setData(1000, rec_id)
            self.ui.listWidget.addItem(item)

    def load_selected_record(self, current, previous):
        if current is None:
            self.selected_id = None
            self.clear_inputs()
            return

        rec_id = current.data(1000)
        self.selected_id = rec_id

        cursor = self.db.conn.cursor()
        cursor.execute("SELECT date, drink_name, glasses, severity, story FROM drinks WHERE id = ?", (rec_id,))
        record = cursor.fetchone()

        if record:
            date, drink, glasses, severity, story = record
            self.ui.whendata.setDate(QtCore.QDate.fromString(date, "yyyy-MM-dd"))
            self.ui.name.setText(drink)
            self.ui.glasses.setValue(glasses)
            self.ui.rate.setValue(severity)
            self.ui.story.setPlainText(story)

    def update_record(self):
        if self.selected_id is None:
            QMessageBox.warning(self, "შეცდომა", "აირჩიე ჩანაწერი შეცვლისთვის.")
            return

        date = self.ui.whendata.date().toString("yyyy-MM-dd")
        name = self.ui.name.text().strip()
        glasses = self.ui.glasses.value()
        severity = self.ui.rate.value()
        story = self.ui.story.toPlainText().strip()

        if not name:
            QMessageBox.warning(self, "შეცდომა", "შეიყვანე სასმელის სახელი.")
            return
        if glasses == 0:
            QMessageBox.warning(self, "შეცდომა", "მიუთითე რამდენი ჭიქა დალიე.")
            return

        cursor = self.db.conn.cursor()
        cursor.execute("""
            UPDATE drinks SET date = ?, drink_name = ?, glasses = ?, severity = ?, story = ?
            WHERE id = ?
        """, (date, name, glasses, severity, story, self.selected_id))
        self.db.conn.commit()

        QMessageBox.information(self, "განახლება", "✅ ჩანაწერი წარმატებით შეიცვალა!")
        self.refresh_records()
        self.clear_inputs()

    def delete_record(self):
        if self.selected_id is None:
            QMessageBox.warning(self, "შეცდომა", "აირჩიე ჩანაწერი წასაშლელად.")
            return

        confirm = QMessageBox.question(self, "წაშლა", "ნამდვილად გინდა ჩანაწერის წაშლა?",
                                       QMessageBox.Yes | QMessageBox.No)
        if confirm == QMessageBox.Yes:
            cursor = self.db.conn.cursor()
            cursor.execute("DELETE FROM drinks WHERE id = ?", (self.selected_id,))
            self.db.conn.commit()
            QMessageBox.information(self, "წაშლა", "✅ ჩანაწერი წაიშალა!")
            self.refresh_records()
            self.clear_inputs()

    def clear_inputs(self):
        self.ui.name.clear()
        self.ui.glasses.setValue(0)
        self.ui.rate.setValue(0)
        self.ui.story.clear()
        self.selected_id = None
        self.ui.whendata.setDate(QtCore.QDate.currentDate())
        self.ui.listWidget.clearSelection()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
