from PyQt5 import QtGui
from PyQt5.Qsci import QsciScintilla
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QPushButton
from PyQt5.QtGui import QPixmap, QIcon

from GlobleData import GlobleData
from Gujrati.mainForm import Ui_MainWindow
from Gujrati.MainQScintilla import MainQScintilla
from Gujrati.TypingQScintilla import TypingQScintilla
from DB import DB


class clsmainForm(QMainWindow):
    closed = pyqtSignal()

    def __init__(self):
        super(clsmainForm, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.txtMainData = MainQScintilla()
        self.txtTypingData = TypingQScintilla()
        self.db = DB()

        self.ui.btn_Back.clicked.connect(self.BackClicked)
        Main_GB_layout = QVBoxLayout()
        Typing_GB_layout = QVBoxLayout()
        Main_GB_layout.addWidget(self.txtMainData)
        Typing_GB_layout.addWidget(self.txtTypingData)

        self.ui.gbMain.setLayout(Main_GB_layout)
        self.ui.gbTyping.setLayout(Typing_GB_layout)
        self.txtTypingData.textChanged.connect(self.TypingDataChange)

        self.ui.btn_tie.setWindowIconText("` ~")
        self.ui.btn_tab.setWindowIconText("1 !")
        self.ui.btn_1.setWindowIconText("2 @")
        self.ui.btn_3.setWindowIconText("3 #")
        self.ui.btn_4.setWindowIconText("4 $")
        self.ui.btn_5.setWindowIconText("5 %")
        self.ui.btn_6.setWindowIconText("6 ^")
        self.ui.btn_7.setWindowIconText("7 &")
        self.ui.btn_8.setWindowIconText("8 *")
        self.ui.btn_9.setWindowIconText("9 (")
        self.ui.btn_0.setWindowIconText("0 )")
        self.ui.btn_minuse.setWindowIconText("- _")
        self.ui.btn_pluse.setWindowIconText("= +")
        self.ui.btn_backspace.setWindowIconText("Backspace")
        self.ui.btn_tab.setWindowIconText("Tab")
        self.ui.btn_Q.setWindowIconText("q Q")
        self.ui.btn_W.setWindowIconText("w W")
        self.ui.btn_E.setWindowIconText("r R")
        self.ui.btn_T.setWindowIconText("t T")
        self.ui.btn_Y.setWindowIconText("y Y")
        self.ui.btn_U.setWindowIconText("u U")
        self.ui.btn_I.setWindowIconText("i I")
        self.ui.btn_O.setWindowIconText("p P")
        self.ui.btn_curlybracket_1.setWindowIconText("[ {")
        self.ui.btn_curlybracket_2.setWindowIconText("] }")
        self.ui.btn_Enter.setWindowIconText("Enter")
        self.ui.btn_capslock.setWindowIconText("capsLock")
        self.ui.btn_A.setWindowIconText("a A")
        self.ui.btn_S.setWindowIconText("s S")
        self.ui.btn_D.setWindowIconText("d D")
        self.ui.btn_F.setWindowIconText("f F")
        self.ui.btn_G.setWindowIconText("h H")
        self.ui.btn_J.setWindowIconText("k K")
        self.ui.btn_L.setWindowIconText("l L")
        self.ui.btn_semicolon.setWindowIconText("; :")
        self.ui.btn_invertedcomma.setWindowIconText(" \" ' ")
        self.ui.btn_slash.setWindowIconText("\ |")
        self.ui.btn_shift_1.setWindowIconText("Shift")
        self.ui.btn_Z.setWindowIconText("z Z")
        self.ui.btn_X.setWindowIconText("x X")
        self.ui.btn_C.setWindowIconText("c C")
        self.ui.btn_V.setWindowIconText("v V")
        self.ui.btn_B.setWindowIconText("b B")
        self.ui.btn_N.setWindowIconText("n N")
        self.ui.btn_M.setWindowIconText("m M")
        self.ui.btn_lessthan.setWindowIconText(", <")
        self.ui.btn_greaterthan.setWindowIconText(". >")
        self.ui.btn_quemark.setWindowIconText("/ ?")
        self.ui.btn_shift_2.setWindowIconText("Shift")
        self.ui.btn_ctrl.setWindowIconText("Ctrl")
        self.ui.btn_win.setWindowIconText("Win")
        self.ui.btn_Alt.setWindowIconText("Alt")
        self.ui.btn_space.setWindowIconText("Space")
        self.ui.btn_Alt_2.setWindowIconText("Alt")
        self.ui.btn_blank.setWindowIconText("Blank")
        self.ui.btn_Ctrl_2.setWindowIconText("Ctrl")

        rows = self.db.runSelect("select Passage from gujrati where Title='" + GlobleData.lesson + "'")
        for row in rows:
            self.txtMainData.setText(row[0])

        self.txtTypingData.setMainText(self.txtMainData.text())
        sp = len(self.txtTypingData.text())
        self.txtMainData.setSelection(0, sp, 0, sp + 1)
        charToShow = self.txtMainData.text()[sp]
        self.txtTypingData.setFocus()
        self.txtMainData.setEnabled(False)

        lefthand = QPixmap('img/handLeft.png')
        righttHand = QPixmap('img/handRight.png')

        self.ui.label_lhand.setPixmap(lefthand)
        self.ui.label_rhand.setPixmap(righttHand)
        self.BtnShowWithBG(charToShow)
        self.ui.btn_tie.setStyleSheet("background-color: white;")
        self.ui.txt_totalchar.setStyleSheet("text-align: center;")
        self.ui.txt_type.setStyleSheet("text-align: center;")

        self.ui.txt_totalchar.setText(str(len(self.txtMainData.text())))
        self.charPressCount = 0

    def BackClicked(self):
        self.closed.emit()
        self.close()

    def styleAt(self, pos):

        return self.txtTypingData.SendScintilla(QsciScintilla.SCI_GETSTYLEAT, pos)

    def TypingDataChange(self):
        try:
            sp = len(self.txtTypingData.text())
            self.txtMainData.setSelection(0, sp, 0, sp + 1)
            charToShow = self.txtMainData.text()[sp]
            self.BtnShowWithBG(charToShow)
            self.ui.txt_totalchar.setText(str(len(self.txtMainData.text())))
            self.charPressCount = int(self.charPressCount) + 1
            self.ui.txt_type.setText(str(self.charPressCount))
            # print(self.styleAt(0))
            i = 0
            currectChar = 0
            wrongChar = 0
            while i < len(self.txtTypingData.text()):
                if self.styleAt(i) == 3:
                    currectChar = int(currectChar) + 1
                if self.styleAt(i) == 1:
                    wrongChar = int(wrongChar) + 1
                i = int(i) + 1
            self.ui.txt_correct.setText(str(currectChar))
            self.ui.txt_wrong.setText(str(wrongChar))
        except:
            pass

    def BtnShowWithBG(self, charToShow):
        for btn in self.ui.gbBtn.findChildren(QPushButton):
            btn.setStyleSheet("background-color: white;")
        for btn in self.ui.lefthand.findChildren(QPushButton):
            btn.setStyleSheet("background-color: white;")
        for btn in self.ui.righthand.findChildren(QPushButton):
            btn.setStyleSheet("background-color: white;")

        if charToShow == " ":
            self.ui.btn_space.setStyleSheet("background-color: aqua;")
        if charToShow.isupper():
            self.ui.btn_shift_1.setStyleSheet("background-color: aqua;")
            self.ui.btn_shift_2.setStyleSheet("background-color: aqua;")
        if charToShow in "~!@#$%^&*()_+{}:\"|<>?|":
            self.ui.btn_shift_1.setStyleSheet("background-color: aqua;")
            self.ui.btn_shift_2.setStyleSheet("background-color: aqua;")

        if charToShow in "~!`1QqAaZz":
            self.ui.btn_lefthand_1.setStyleSheet("background-color: aqua;")
        if charToShow in "~!@WSX2wsx":
            self.ui.btn_lefthand_2.setStyleSheet("background-color: aqua;")
        if charToShow in "#EDC3edc":
            self.ui.btn_lefthand_3.setStyleSheet("background-color: aqua;")
        if charToShow in "$RFV%TGB4rfv5tgb":
            self.ui.btn_lefthand_4.setStyleSheet("background-color: aqua;")

        if charToShow in "P:?|\"{}|p;/['\]\\_+-=":
            self.ui.btn_righthand_1.setStyleSheet("background-color: aqua;")
        if charToShow in "(OL>.lo9)0":
            self.ui.btn_righthand_2.setStyleSheet("background-color: aqua;")
        if charToShow in "*IK<,ki8":
            self.ui.btn_righthand_3.setStyleSheet("background-color: aqua;")
        if charToShow in "^YHN&UJM6yhn7ujm":
            self.ui.btn_rigthhand_4.setStyleSheet("background-color: aqua;")

        for btn in self.ui.gbBtn.findChildren(QPushButton):
            ans = btn.text().split()
            try:
                # print(ans[0] +"   -     "+ ans[1])
                if len(ans) >= 2:
                    if charToShow == ans[0] or charToShow == ans[1]:
                        print(btn.text())
                        btn.setStyleSheet("background-color: aqua;")
            except:
                pass
            # if charToShow in btn.text():
            #     print(btn.text())
