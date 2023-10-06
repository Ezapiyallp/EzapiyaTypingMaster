import sqlite3

from PyQt5 import QtGui, QtWidgets, QtCore
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QMessageBox

from new_session_form import Ui_MainWindow
from GlobleData import GlobleData
from DB import DB
from english.clsmainForm import clsmainForm as clsEnglish
from marathi.clsmainForm import clsmainForm as clsMarathi
from hindi.clsmainForm import clsmainForm as clsHindi
from ajgar.clsmainForm import clsmainForm as clsAjgar
from Gujrati.clsmainForm import clsmainForm as clsGujrati
from Panjabi.clsmainForm import clsmainForm as clsPanjabi


class cls_new_session_form(QtWidgets.QMainWindow):
    closed = pyqtSignal()

    def __init__(self):
        super(cls_new_session_form, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.db = DB()
        self.englishForm = None
        self.marathiForm = None
        self.hindiForm = None
        self.ajgarForm = None
        self.panjabiform = None
        self.gujratiform = None
        self.f = None
        self.selectedChapter = ""
        self.ui.btn_back.clicked.connect(self.BackClicked)
        self.ui.btn_Start.clicked.connect(self.StartClicked)
        self.ui.lstChapter.clear()
        man = QPixmap('img/gentleman.svg')
        self.ui.label_man.setPixmap(man)

        #
        self.ui.lstChapter.itemClicked.connect(self.lstChapter_itemClick)

        if GlobleData.language == "english":
            rows = self.db.runSelect("select Title from English")
            for row in rows:
                # print(row[0])
                self.ui.lstChapter.addItem(row[0])

        if GlobleData.language == "hindi":
            rows = self.db.runSelect("select Title from hindi")
            for row in rows:
                # print(row[0])
                self.ui.lstChapter.addItem(row[0])
        if GlobleData.language == "marathi":
            rows = self.db.runSelect("select Title from marathi")
            for row in rows:
                # print(row[0])
                self.ui.lstChapter.addItem(row[0])
        if GlobleData.language == "ajgar":
            rows = self.db.runSelect("select Title from Ajagar_Font")
            for row in rows:
                # print(row[0])
                self.ui.lstChapter.addItem(row[0])
        if GlobleData.language == "gujrati":
            rows = self.db.runSelect("select Title from gujrati")
            for row in rows:
                # print(row[0])
                self.ui.lstChapter.addItem(row[0])
        if GlobleData.language == "panjabi":
            rows = self.db.runSelect("select Title from panjabi")
            for row in rows:
                # print(row[0])
                self.ui.lstChapter.addItem(row[0])

    def lstChapter_itemClick(self, item):
        print(item.text())
        self.selectedChapter = item.text()

    def BackClicked(self):
        self.closed.emit()
        self.close()

    def StartClicked(self):
        if self.selectedChapter == "":
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("Please Select Lesson")
            msg.setWindowTitle("Information")
            msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            retval = msg.exec_()
        else:
            GlobleData.lesson = self.selectedChapter
            if GlobleData.language == "english":
                self.englishForm = clsEnglish()
                self.englishForm.closed.connect(self.ChiledClose)
                self.englishForm.show()
                self.hide()
            if GlobleData.language == "hindi":
                self.hindiForm = clsHindi()
                self.hindiForm.closed.connect(self.ChiledClose)
                self.hindiForm.show()
                self.hide()
            if GlobleData.language == "marathi":
                self.marathiForm = clsMarathi()
                self.marathiForm.show()
                self.marathiForm.closed.connect(self.ChiledClose)
                self.hide()
            if GlobleData.language == "ajgar":
                self.ajgarForm = clsAjgar()
                self.ajgarForm.closed.connect(self.ChiledClose)
                self.ajgarForm.show()
                self.hide()
            if GlobleData.language == "gujrati":
                self.gujratiform = clsGujrati()
                self.gujratiform.closed.connect(self.ChiledClose)
                self.gujratiform.show()
                self.hide()
            if GlobleData.language == "panjabi":
                self.panjabiform = clsPanjabi()
                self.panjabiform.closed.connect(self.ChiledClose)
                self.panjabiform.show()
                self.hide()

    def ChiledClose(self):
        print("hkey")
        self.show()
