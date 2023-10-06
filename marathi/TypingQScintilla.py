from PyQt5 import QtCore
from PyQt5.Qsci import QsciScintilla, QsciLexerCPP, QsciLexerCustom
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import QFont, QColor


class MyLexer(QsciLexerCustom):

    def __init__(self, parent):
        super(MyLexer, self).__init__(parent)

        # Default text settings
        # ----------------------
        self.setDefaultColor(QColor("#ff000000"))
        self.setDefaultPaper(QColor("#ffffffff"))
        self.setDefaultFont(QFont("Kruti Dev 010", 14))

        # Initialize colors per style
        # ----------------------------
        self.setColor(QColor("#ff000000"), 0)   # Style 0: black
        self.setColor(QColor("#ff7f0000"), 1)   # Style 1: red
        self.setColor(QColor("#ff0000bf"), 2)   # Style 2: blue
        self.setColor(QColor("#ff007f00"), 3)   # Style 3: green

        # Initialize paper colors per style
        # ----------------------------------
        self.setPaper(QColor("#ffffffff"), 0)   # Style 0: white
        self.setPaper(QColor("#ffffffff"), 1)   # Style 1: white
        self.setPaper(QColor("#ffffffff"), 2)   # Style 2: white
        self.setPaper(QColor("#ffffffff"), 3)   # Style 3: white

        # Initialize fonts per style
        # ---------------------------
        self.setFont(QFont("Kruti Dev 010", 14, weight=QFont.Bold), 0)   # Style 0: Consolas 14pt
        self.setFont(QFont("Kruti Dev 010", 14, weight=QFont.Bold), 1)   # Style 1: Consolas 14pt
        self.setFont(QFont("Kruti Dev 010", 14, weight=QFont.Bold), 2)   # Style 2: Consolas 14pt
        self.setFont(QFont("Kruti Dev 010", 14, weight=QFont.Bold), 3)   # Style 3: Consolas 14pt

        # Auto indent
        # ------------


    ''''''

    def language(self):
        return "SimpleLanguage"
    ''''''

    def description(self, style):
        if style == 0:
            return "myStyle_0"
        elif style == 1:
            return "myStyle_1"
        elif style == 2:
            return "myStyle_2"
        elif style == 3:
            return "myStyle_3"
        ###
        return ""
    ''''''

    def styleText(self, start, end):
         # text = self.parent().text()[ll:end]
        MainText= self.parent().MainText
        typingText=self.parent().text()
        wordCount= len(typingText)
        chart= typingText[wordCount-1]
        charo=MainText[wordCount-1]
        print(chart +" "+charo)
        if chart==charo:
            self.setStyling(1, 3)
        else:
            self.setStyling(1, 1)
    ''''''

''' end Class '''


class TypingQScintilla(QsciScintilla):
    def __init__(self, parent=None):
        super(TypingQScintilla, self).__init__(parent)

        self.MainText=""
        self.charCount=0
        font = QFont()
        font.setFamily('ezapiya1')
        font.setFixedPitch(True)
        font.setPointSize(16)
        self.setFont(font)
        self.lexer = MyLexer(self)
        self.setLexer(self.lexer)



    def setMainText(self,text):
        self.MainText=text



