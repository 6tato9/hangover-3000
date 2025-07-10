from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(887, 808)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.add = QtWidgets.QPushButton(self.centralwidget)
        self.add.setGeometry(QtCore.QRect(40, 680, 251, 61))
        self.add.setObjectName("add")

        self.update = QtWidgets.QPushButton(self.centralwidget)
        self.update.setGeometry(QtCore.QRect(340, 680, 221, 61))
        self.update.setObjectName("update")

        self.delete_2 = QtWidgets.QPushButton(self.centralwidget)
        self.delete_2.setGeometry(QtCore.QRect(620, 680, 221, 61))
        self.delete_2.setAutoDefault(False)
        self.delete_2.setObjectName("delete_2")

        self.name = QtWidgets.QLineEdit(self.centralwidget)
        self.name.setGeometry(QtCore.QRect(210, 510, 121, 31))
        self.name.setText("")
        self.name.setObjectName("name")

        self.whendata = QtWidgets.QDateEdit(self.centralwidget)
        self.whendata.setGeometry(QtCore.QRect(30, 510, 141, 31))
        self.whendata.setCalendarPopup(True)
        self.whendata.setObjectName("whendata")

        self.rate = QtWidgets.QSpinBox(self.centralwidget)
        self.rate.setGeometry(QtCore.QRect(620, 510, 201, 31))
        self.rate.setRange(0, 10)
        self.rate.setObjectName("rate")

        self.story = QtWidgets.QTextEdit(self.centralwidget)
        self.story.setGeometry(QtCore.QRect(30, 580, 831, 87))
        self.story.setObjectName("story")

        self.when = QtWidgets.QLabel(self.centralwidget)
        self.when.setGeometry(QtCore.QRect(30, 460, 161, 51))
        self.when.setObjectName("when")

        self.what = QtWidgets.QLabel(self.centralwidget)
        self.what.setGeometry(QtCore.QRect(210, 450, 171, 71))
        self.what.setObjectName("what")

        self.howmany = QtWidgets.QLabel(self.centralwidget)
        self.howmany.setGeometry(QtCore.QRect(350, 470, 211, 31))
        self.howmany.setObjectName("howmany")

        self.glasses = QtWidgets.QSpinBox(self.centralwidget)
        self.glasses.setGeometry(QtCore.QRect(350, 510, 191, 31))
        self.glasses.setRange(0, 100)
        self.glasses.setObjectName("glasses")

        self.onetoten = QtWidgets.QLabel(self.centralwidget)
        self.onetoten.setGeometry(QtCore.QRect(580, 470, 261, 31))
        self.onetoten.setObjectName("onetoten")

        self.whatidid = QtWidgets.QLabel(self.centralwidget)
        self.whatidid.setGeometry(QtCore.QRect(30, 550, 301, 31))
        self.whatidid.setObjectName("whatidid")

        # QTextBrowser ჩანაცვლებულია QListWidget-ით
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(20, 10, 841, 461))
        self.listWidget.setObjectName("listWidget")

        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 887, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Hangover Helper 3000"))
        self.add.setText(_translate("MainWindow", "დამატება"))
        self.update.setText(_translate("MainWindow", "შეცვლა"))
        self.delete_2.setText(_translate("MainWindow", "წაშლა"))
        self.when.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">როდის დავლიე?</span></p></body></html>"))
        self.what.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">რა დავლიე?</span></p></body></html>"))
        self.howmany.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">რამდენი ჭიქა დავლიე?</span></p></body></html>"))
        self.onetoten.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">რამდენად დავთვერი (1-10)</span></p></body></html>"))
        self.whatidid.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt;\">რა გავაკეთე სისულელე?</span></p></body></html>"))
