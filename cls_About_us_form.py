from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QMainWindow

from About_us_form import Ui_MainWindow


class cls_About_us_form(QMainWindow):
    closed = pyqtSignal()

    def __init__(self):
        super(cls_About_us_form, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.btn_back.clicked.connect(self.BackClicked)

    def BackClicked(self):
        self.closed.emit()
        self.close()