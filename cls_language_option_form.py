from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import QPixmap, QIcon

from cls_About_us_form import cls_About_us_form
from cls_new_session_form import cls_new_session_form
from language_option_form import Ui_MainWindow
from GlobleData import GlobleData


class cls_language_option_form(QtWidgets.QMainWindow):
    closed = pyqtSignal()

    def __init__(self):
        super(cls_language_option_form, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.f3 = None
        self.f4 = None

        self.ui.btn_english.clicked.connect(self.englishClicked)
        self.ui.btn_hindi.clicked.connect(self.hindiClicked)
        self.ui.btn_marathi.clicked.connect(self.marathiClicked)
        self.ui.btn_font.clicked.connect(self.fontClicked)
        self.ui.btn_punjabi.clicked.connect(self.punjabiClicked)
        self.ui.btn_gujarti.clicked.connect(self.gujaratiClicked)
        self.ui.btn_about_us.clicked.connect(self.about_usClicked)

        work = QPixmap('img/lady.png')
        self.ui.label_girl_2.setPixmap(work)
        girl = QPixmap('img/images.png')
        self.ui.label_girl.setPixmap(girl)

    def englishClicked(self):
        GlobleData.language = "english"
        self.f3 = cls_new_session_form()
        self.f3.closed.connect(self.ChiledClose)
        self.f3.show()
        self.hide()

    def ChiledClose(self):
        print("hjkhj")
        self.show()

    def hindiClicked(self):
        GlobleData.language = "hindi"
        self.f3 = cls_new_session_form()
        self.f3.closed.connect(self.ChiledClose)
        self.f3.show()
        self.hide()

    def ChiledClose(self):
        print("hjkhj")
        self.show()

    def marathiClicked(self):
        GlobleData.language = "marathi"
        self.f3 = cls_new_session_form()
        self.f3.closed.connect(self.ChiledClose)
        self.f3.show()
        self.hide()

    def ChiledClose(self):
        print("hjkhj")
        self.show()

    def fontClicked(self):
        GlobleData.language = "ajgar"
        self.f3 = cls_new_session_form()
        self.f3.closed.connect(self.ChiledClose)
        self.f3.show()
        self.hide()

    def ChiledClose(self):
        print("hjkhj")
        self.show()

    def punjabiClicked(self):
        GlobleData.language = "panjabi"
        self.f3 = cls_new_session_form()
        self.f3.closed.connect(self.ChiledClose)
        self.f3.show()
        self.hide()

    def ChiledClose(self):
        print("hjkhj")
        self.show()

    def gujaratiClicked(self):
        GlobleData.language = "gujrati"
        self.f3 = cls_new_session_form()
        self.f3.closed.connect(self.ChiledClose)
        self.f3.show()
        self.hide()

    def ChiledClose(self):
        print("hjkhj")
        self.show()

    def about_usClicked(self):
        self.f4 = cls_About_us_form()
        self.f4.closed.connect(self.ChiledClose)
        self.f4.show()
        self.hide()

    def ChiledClose(self):
        print("hjkhj")
        self.show()
