from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSignal

from key_form import Ui_MainWindow


class cls_key_form(QtWidgets.QMainWindow):
    closed = pyqtSignal()

    def __init__(self):
        super(cls_key_form, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.btn_close.clicked.connect(self.closeClicked)

        self.ui.btn_0153.setIcon(QtGui.QIcon('keyimages/0153.png'))
        self.ui.btn_0153.setIconSize(QtCore.QSize(60, 60))

        self.ui.btn_0159.setIcon(QtGui.QIcon('keyimages/0159.png'))
        self.ui.btn_0159.setIconSize(QtCore.QSize(60, 60))

        self.ui.btn_0161.setIcon(QtGui.QIcon('keyimages/0161.png'))
        self.ui.btn_0161.setIconSize(QtCore.QSize(60, 60))

        self.ui.btn_0162.setIcon(QtGui.QIcon('keyimages/0162.png'))
        self.ui.btn_0162.setIconSize(QtCore.QSize(60, 60))

        self.ui.btn_0163.setIcon(QtGui.QIcon('keyimages/0163.png'))
        self.ui.btn_0163.setIconSize(QtCore.QSize(60, 60))

        self.ui.btn_0164.setIcon(QtGui.QIcon('keyimages/0164.png'))
        self.ui.btn_0164.setIconSize(QtCore.QSize(60, 60))

        # self.ui.btn_0165.setIcon(QtGui.QIcon('keyimages/0165.png'))
        # self.ui.btn_0165.setIconSize(QtCore.QSize(60, 60))

        self.ui.btn_0170.setIcon(QtGui.QIcon('keyimages/0170.png'))
        self.ui.btn_0170.setIconSize(QtCore.QSize(60, 60))

        self.ui.btn_0171.setIcon(QtGui.QIcon('keyimages/0171.png'))
        self.ui.btn_0171.setIconSize(QtCore.QSize(60, 60))

        self.ui.btn_0177.setIcon(QtGui.QIcon('keyimages/0177.png'))
        self.ui.btn_0177.setIconSize(QtCore.QSize(60, 60))

        self.ui.btn_0179.setIcon(QtGui.QIcon('keyimages/0179.png'))
        self.ui.btn_0179.setIconSize(QtCore.QSize(60, 60))

        self.ui.btn_0180.setIcon(QtGui.QIcon('keyimages/0180.png'))
        self.ui.btn_0180.setIconSize(QtCore.QSize(60, 60))

        self.ui.btn_0182.setIcon(QtGui.QIcon('keyimages/0182.png'))
        self.ui.btn_0182.setIconSize(QtCore.QSize(60, 60))

        self.ui.btn_0183.setIcon(QtGui.QIcon('keyimages/0183.png'))
        self.ui.btn_0183.setIconSize(QtCore.QSize(60, 60))

        self.ui.btn_0184.setIcon(QtGui.QIcon('keyimages/0184.png'))
        self.ui.btn_0184.setIconSize(QtCore.QSize(60, 60))

        self.ui.btn_0186.setIcon(QtGui.QIcon('keyimages/0186.png'))
        self.ui.btn_0186.setIconSize(QtCore.QSize(60, 60))

        self.ui.btn_0197.setIcon(QtGui.QIcon('keyimages/0197.png'))
        self.ui.btn_0197.setIconSize(QtCore.QSize(60, 60))

        self.ui.btn_0204.setIcon(QtGui.QIcon('keyimages/0204.png'))
        self.ui.btn_0204.setIconSize(QtCore.QSize(60, 60))

        self.ui.btn_0205.setIcon(QtGui.QIcon('keyimages/0205.png'))
        self.ui.btn_0205.setIconSize(QtCore.QSize(60, 60))

        self.ui.btn_0206.setIcon(QtGui.QIcon('keyimages/0206.png'))
        self.ui.btn_0206.setIconSize(QtCore.QSize(60, 60))

        self.ui.btn_0207.setIcon(QtGui.QIcon('keyimages/0207.png'))
        self.ui.btn_0207.setIconSize(QtCore.QSize(60, 60))

        self.ui.btn_0211.setIcon(QtGui.QIcon('keyimages/0211.png'))
        self.ui.btn_0211.setIconSize(QtCore.QSize(60, 60))

        self.ui.btn_0212.setIcon(QtGui.QIcon('keyimages/0212.png'))
        self.ui.btn_0212.setIconSize(QtCore.QSize(60, 60))

        self.ui.btn_0214.setIcon(QtGui.QIcon('keyimages/0214.png'))
        self.ui.btn_0214.setIconSize(QtCore.QSize(60, 60))

        self.ui.btn_0216.setIcon(QtGui.QIcon('keyimages/0216.png'))
        self.ui.btn_0216.setIconSize(QtCore.QSize(60, 60))

        # self.ui.btn_0217.setIcon(QtGui.QIcon('keyimages/0217.png'))
        # self.ui.btn_0217.setIconSize((QtCore.QSize(60, 60)))

        self.ui.btn_0220.setIcon(QtGui.QIcon('keyimages/0220.png'))
        self.ui.btn_0220.setIconSize(QtCore.QSize(60, 60))

        self.ui.btn_0221.setIcon(QtGui.QIcon('keyimages/0221.png'))
        self.ui.btn_0221.setIconSize(QtCore.QSize(60, 60))

        self.ui.btn_0224.setIcon(QtGui.QIcon('keyimages/0224.png'))
        self.ui.btn_0224.setIconSize(QtCore.QSize(60, 60))

        self.ui.btn_0225.setIcon(QtGui.QIcon('keyimages/0225.png'))
        self.ui.btn_0225.setIconSize(QtCore.QSize(60, 60))

        self.ui.btn_0226.setIcon(QtGui.QIcon('keyimages/0226.png'))
        self.ui.btn_0226.setIconSize(QtCore.QSize(60, 60))

        self.ui.btn_0227.setIcon(QtGui.QIcon('keyimages/0227.png'))
        self.ui.btn_0227.setIconSize(QtCore.QSize(60, 60))

        self.ui.btn_0228.setIcon(QtGui.QIcon('keyimages/0228.png'))
        self.ui.btn_0228.setIconSize(QtCore.QSize(60, 60))

        self.ui.btn_0233.setIcon(QtGui.QIcon('keyimages/0233.png'))
        self.ui.btn_0233.setIconSize(QtCore.QSize(60, 60))

        self.ui.btn_0244.setIcon(QtGui.QIcon('keyimages/0244.png'))
        self.ui.btn_0244.setIconSize(QtCore.QSize(60, 60))

        self.ui.btn_0246.setIcon(QtGui.QIcon('keyimages/0246.png'))
        self.ui.btn_0246.setIconSize(QtCore.QSize(60, 60))

        # self.ui.btn_0247.setIcon(QtGui.QIcon('keyimages/0247.png'))
        # self.ui.btn_0247.setIconSize(QtCore.QSize(60, 60))

        self.ui.btn_0249.setIcon(QtGui.QIcon('keyimages/0249.png'))
        self.ui.btn_0249.setIconSize(QtCore.QSize(60, 60))

        self.ui.btn_1451.setIcon(QtGui.QIcon('keyimages/1451.png'))
        self.ui.btn_1451.setIconSize(QtCore.QSize(60, 60))

        # self.ui.btn_1452.setIcon(QtGui.QIcon('keyimages/1452.png'))
        # self.ui.btn_1452.setIconSize(QtCore.QSize(60, 60))

        # self.ui.btn_1461.setIcon(QtGui.QIcon('keyimages/1461.png'))
        # self.ui.btn_1461.setIconSize(QtCore.QSize(60, 60))

        self.ui.btn_1462.setIcon(QtGui.QIcon('keyimages/1462.png'))
        self.ui.btn_1462.setIconSize(QtCore.QSize(60, 60))

        # self.ui.btn_1471.setIcon(QtGui.QIcon('keyimages/1471.png'))
        # self.ui.btn_1471.setIconSize(QtCore.QSize(60, 60))

        self.ui.btn_1472.setIcon(QtGui.QIcon('keyimages/1472.png'))
        self.ui.btn_1472.setIconSize(QtCore.QSize(100, 100))

        self.ui.btn_0187.setIcon(QtGui.QIcon('keyimages/0187.png'))
        self.ui.btn_0187.setIconSize(QtCore.QSize(60, 60))

        self.ui.btn_1482.setIcon(QtGui.QIcon('keyimages/1482.png'))
        self.ui.btn_1482.setIconSize(QtCore.QSize(60, 60))

        # self.ui.btn_01531.setIcon(QtGui.QIcon('keyimages/01531.png'))
        # self.ui.btn_01531.setIconSize(QtCore.QSize(60, 60))

        # self.ui.btn_01831.setIcon(QtGui.QIcon('keyimages/01831.png'))
        # self.ui.btn_01831.setIconSize(QtCore.QSize(60, 60))

        self.ui.btn_02181.setIcon(QtGui.QIcon('keyimages/02181.png'))
        self.ui.btn_02181.setIconSize(QtCore.QSize(60, 60))

        # self.ui.btn_02111.setIcon(QtGui.QIcon('keyimages/02111.png'))
        # self.ui.btn_02111.setIconSize(QtCore.QSize(60, 60))
    def closeClicked(self):
        self.closed.emit()
        self.close()
