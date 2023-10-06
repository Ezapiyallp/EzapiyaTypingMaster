from PyQt5 import QtGui, QtCore
from PyQt5.Qsci import QsciScintilla
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QPushButton
from PyQt5.QtGui import QPixmap, QIcon

from GlobleData import GlobleData
from ajgar.mainForm import Ui_MainWindow
from ajgar.MainQScintilla import MainQScintilla
from ajgar.TypingQScintilla import TypingQScintilla
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

        Main_GB_layout = QVBoxLayout()
        Typing_GB_layout = QVBoxLayout()
        Main_GB_layout.addWidget(self.txtMainData)
        Typing_GB_layout.addWidget(self.txtTypingData)

        self.ui.btn_back.clicked.connect(self.BackClicked)
        self.ui.gbMain.setLayout(Main_GB_layout)
        self.ui.gbTyping.setLayout(Typing_GB_layout)
        self.txtTypingData.textChanged.connect(self.TypingDataChange)

        self.ui.btn_tie.setWindowIconText("` ~")
        self.ui.btn_1.setWindowIconText("1 !")
        self.ui.btn_2.setWindowIconText("2 @")
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
        self.ui.btn_E.setWindowIconText("e E")
        self.ui.btn_R.setWindowIconText("r R")
        self.ui.btn_T.setWindowIconText("t T")
        self.ui.btn_Y.setWindowIconText("y Y")
        self.ui.btn_U.setWindowIconText("u U")
        self.ui.btn_I.setWindowIconText("i I")
        self.ui.btn_O.setWindowIconText("o O")
        self.ui.btn_P.setWindowIconText("p P")
        self.ui.btn_curlybracket_1.setWindowIconText("[ {")
        self.ui.btn_curlybracket_2.setWindowIconText("] }")
        self.ui.btn_Enter.setWindowIconText("Enter")
        self.ui.btn_capslock.setWindowIconText("capsLock")
        self.ui.btn_A.setWindowIconText("a A")
        self.ui.btn_S.setWindowIconText("s S")
        self.ui.btn_D.setWindowIconText("d D")
        self.ui.btn_F.setWindowIconText("f F")
        self.ui.btn_G.setWindowIconText("g G")
        self.ui.btn_H.setWindowIconText("h H")
        self.ui.btn_J.setWindowIconText("j J")
        self.ui.btn_K.setWindowIconText("k K")
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

        self.ui.btn_tie.setText("")
        self.ui.btn_1.setText("")
        self.ui.btn_2.setText("")
        self.ui.btn_3.setText("")
        self.ui.btn_4.setText("")
        self.ui.btn_5.setText("")
        self.ui.btn_6.setText("")
        self.ui.btn_7.setText("")
        self.ui.btn_8.setText("")
        self.ui.btn_9.setText("")
        self.ui.btn_0.setText("")
        self.ui.btn_minuse.setText("")
        self.ui.btn_pluse.setText("")

        self.ui.btn_tie.setIcon(QtGui.QIcon('ajgarFontImage/_`.png'))
        self.ui.btn_tie.setIconSize(QtCore.QSize(60, 60))

        self.ui.btn_1.setIcon(QtGui.QIcon('ajgarFontImage/_1.png'))
        self.ui.btn_1.setIconSize(QtCore.QSize(60, 60))

        self.ui.btn_2.setIcon(QtGui.QIcon('ajgarFontImage/_2.png'))
        self.ui.btn_2.setIconSize(QtCore.QSize(60, 60))

        self.ui.btn_3.setIcon(QtGui.QIcon('ajgarFontImage/_3.png'))
        self.ui.btn_3.setIconSize(QtCore.QSize(60, 60))

        self.ui.btn_4.setIcon(QtGui.QIcon('ajgarFontImage/_4.png'))
        self.ui.btn_4.setIconSize(QtCore.QSize(60, 60))

        self.ui.btn_5.setIcon(QtGui.QIcon('ajgarFontImage/_5.png'))
        self.ui.btn_5.setIconSize(QtCore.QSize(60, 60))

        self.ui.btn_6.setIcon(QtGui.QIcon('ajgarFontImage/_6.png'))
        self.ui.btn_6.setIconSize(QtCore.QSize(60, 60))

        self.ui.btn_7.setIcon(QtGui.QIcon('ajgarFontImage/_7.png'))
        self.ui.btn_7.setIconSize(QtCore.QSize(60, 60))

        self.ui.btn_8.setIcon(QtGui.QIcon('ajgarFontImage/_8.png'))
        self.ui.btn_8.setIconSize(QtCore.QSize(60, 60))

        self.ui.btn_9.setIcon(QtGui.QIcon('ajgarFontImage/_9.png'))
        self.ui.btn_9.setIconSize(QtCore.QSize(60, 60))

        self.ui.btn_0.setIcon(QtGui.QIcon('ajgarFontImage/_0.png'))
        self.ui.btn_0.setIconSize(QtCore.QSize(60, 60))

        self.ui.btn_minuse.setIcon(QtGui.QIcon('ajgarFontImage/__.png'))
        self.ui.btn_minuse.setIconSize(QtCore.QSize(60, 60))

        self.ui.btn_pluse.setIcon(QtGui.QIcon('ajgarFontImage/_+.png'))
        self.ui.btn_pluse.setIconSize(QtCore.QSize(60, 60))

        self.ui.btn_Q.setText("")
        self.ui.btn_W.setText("")
        self.ui.btn_E.setText("")
        self.ui.btn_R.setText("")
        self.ui.btn_T.setText("")
        self.ui.btn_Y.setText("")
        self.ui.btn_U.setText("")
        self.ui.btn_I.setText("")
        self.ui.btn_O.setText("")
        self.ui.btn_P.setText("")
        self.ui.btn_curlybracket_1.setText("")
        self.ui.btn_curlybracket_2.setText("")

        self.ui.btn_Q.setIcon(QtGui.QIcon('ajgarFontImage/q.png'))
        self.ui.btn_Q.setIconSize(QtCore.QSize(60, 60))

        self.ui.btn_W.setIcon(QtGui.QIcon('ajgarFontImage/w.png'))
        self.ui.btn_W.setIconSize(QtCore.QSize(60, 60))

        self.ui.btn_E.setIcon(QtGui.QIcon('ajgarFontImage/e.png'))
        self.ui.btn_E.setIconSize(QtCore.QSize(60, 60))

        self.ui.btn_R.setIcon(QtGui.QIcon('ajgarFontImage/r.png'))
        self.ui.btn_R.setIconSize(QtCore.QSize(60, 60))

        self.ui.btn_T.setIcon(QtGui.QIcon('ajgarFontImage/t.png'))
        self.ui.btn_T.setIconSize(QtCore.QSize(60, 60))

        self.ui.btn_Y.setIcon(QtGui.QIcon('ajgarFontImage/y.png'))
        self.ui.btn_Y.setIconSize(QtCore.QSize(60, 60))

        self.ui.btn_U.setIcon(QtGui.QIcon('ajgarFontImage/u.png'))
        self.ui.btn_U.setIconSize(QtCore.QSize(60, 60))

        self.ui.btn_I.setIcon(QtGui.QIcon('ajgarFontImage/i.png'))
        self.ui.btn_I.setIconSize(QtCore.QSize(60, 60))

        self.ui.btn_O.setIcon(QtGui.QIcon('ajgarFontImage/o.png'))
        self.ui.btn_O.setIconSize(QtCore.QSize(60, 60))

        self.ui.btn_P.setIcon(QtGui.QIcon('ajgarFontImage/p.png'))
        self.ui.btn_P.setIconSize(QtCore.QSize(60, 60))

        self.ui.btn_curlybracket_1.setIcon(QtGui.QIcon('ajgarFontImage/_[.png'))
        self.ui.btn_curlybracket_1.setIconSize(QtCore.QSize(60, 60))

        self.ui.btn_curlybracket_2.setIcon(QtGui.QIcon('ajgarFontImage/_].png'))
        self.ui.btn_curlybracket_2.setIconSize(QtCore.QSize(60, 60))

        self.ui.btn_A.setText("")
        self.ui.btn_S.setText("")
        self.ui.btn_D.setText("")
        self.ui.btn_F.setText("")
        self.ui.btn_G.setText("")
        self.ui.btn_H.setText("")
        self.ui.btn_J.setText("")
        self.ui.btn_K.setText("")
        self.ui.btn_L.setText("")
        self.ui.btn_semicolon.setText("")
        self.ui.btn_invertedcomma.setText("")
        self.ui.btn_slash.setText("")

        self.ui.btn_A.setIcon(QtGui.QIcon('ajgarFontImage/a.png'))
        self.ui.btn_A.setIconSize(QtCore.QSize(60, 60))

        self.ui.btn_S.setIcon(QtGui.QIcon('ajgarFontImage/s.png'))
        self.ui.btn_S.setIconSize(QtCore.QSize(60, 60))

        self.ui.btn_D.setIcon(QtGui.QIcon('ajgarFontImage/d.png'))
        self.ui.btn_D.setIconSize(QtCore.QSize(60, 60))

        self.ui.btn_F.setIcon(QtGui.QIcon('ajgarFontImage/f.png'))
        self.ui.btn_F.setIconSize(QtCore.QSize(60, 60))

        self.ui.btn_G.setIcon(QtGui.QIcon('ajgarFontImage/g.png'))
        self.ui.btn_G.setIconSize(QtCore.QSize(60, 60))

        self.ui.btn_H.setIcon(QtGui.QIcon('ajgarFontImage/h.png'))
        self.ui.btn_H.setIconSize(QtCore.QSize(60, 60))

        self.ui.btn_J.setIcon(QtGui.QIcon('ajgarFontImage/j.png'))
        self.ui.btn_J.setIconSize(QtCore.QSize(60, 60))

        self.ui.btn_K.setIcon(QtGui.QIcon('ajgarFontImage/k.png'))
        self.ui.btn_K.setIconSize(QtCore.QSize(60, 60))

        self.ui.btn_L.setIcon(QtGui.QIcon('ajgarFontImage/l.png'))
        self.ui.btn_L.setIconSize(QtCore.QSize(60, 60))

        self.ui.btn_semicolon.setIcon(QtGui.QIcon('ajgarFontImage/_;.png'))
        self.ui.btn_semicolon.setIconSize(QtCore.QSize(60, 60))

        self.ui.btn_invertedcomma.setIcon(QtGui.QIcon('ajgarFontImage/kkk.png'))
        self.ui.btn_invertedcomma.setIconSize(QtCore.QSize(60, 60))

        self.ui.btn_slash.setIcon(QtGui.QIcon('ajgarFontImage/aaa.png'))
        self.ui.btn_slash.setIconSize(QtCore.QSize(60, 60))

        self.ui.btn_Z.setText("")
        self.ui.btn_X.setText("")
        self.ui.btn_C.setText("")
        self.ui.btn_V.setText("")
        self.ui.btn_B.setText("")
        self.ui.btn_N.setText("")
        self.ui.btn_M.setText("")
        self.ui.btn_lessthan.setText("")
        self.ui.btn_greaterthan.setText("")
        self.ui.btn_quemark.setText("")

        self.ui.btn_Z.setIcon(QtGui.QIcon('ajgarFontImage/z.png'))
        self.ui.btn_Z.setIconSize(QtCore.QSize(60, 60))

        self.ui.btn_X.setIcon(QtGui.QIcon('ajgarFontImage/x.png'))
        self.ui.btn_X.setIconSize(QtCore.QSize(60, 60))

        self.ui.btn_C.setIcon(QtGui.QIcon('ajgarFontImage/c.png'))
        self.ui.btn_C.setIconSize(QtCore.QSize(60, 60))

        self.ui.btn_V.setIcon(QtGui.QIcon('ajgarFontImage/v.png'))
        self.ui.btn_V.setIconSize(QtCore.QSize(60, 60))

        self.ui.btn_B.setIcon(QtGui.QIcon('ajgarFontImage/b.png'))
        self.ui.btn_B.setIconSize(QtCore.QSize(60, 60))

        self.ui.btn_N.setIcon(QtGui.QIcon('ajgarFontImage/n.png'))
        self.ui.btn_N.setIconSize(QtCore.QSize(60, 60))

        self.ui.btn_M.setIcon(QtGui.QIcon('ajgarFontImage/m.png'))
        self.ui.btn_M.setIconSize(QtCore.QSize(60, 60))

        self.ui.btn_lessthan.setIcon(QtGui.QIcon('ajgarFontImage/_,.png'))
        self.ui.btn_lessthan.setIconSize(QtCore.QSize(60, 60))

        self.ui.btn_greaterthan.setIcon(QtGui.QIcon('ajgarFontImage/_gt.png'))
        self.ui.btn_greaterthan.setIconSize(QtCore.QSize(60, 60))

        self.ui.btn_quemark.setIcon(QtGui.QIcon('ajgarFontImage/bbb.png'))
        self.ui.btn_quemark.setIconSize(QtCore.QSize(60, 60))

        ########################
        rows = self.db.runSelect("select Passage from Ajagar_Font where Title='" + GlobleData.lesson + "'")
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
            # ans= btn.text().split()
            ans = btn.windowIconText().split()

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
