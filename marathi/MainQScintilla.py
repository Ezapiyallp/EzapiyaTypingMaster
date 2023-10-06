from PyQt5.Qsci import QsciScintilla, QsciLexerCPP
from PyQt5.QtGui import QFont


class MainQScintilla(QsciScintilla):
    def __init__(self, parent=None):
        super(MainQScintilla, self).__init__(parent)
        font = QFont()
        font.setFamily('Kruti Dev 010')
        font.setFixedPitch(True)
        font.setPointSize(16)
        self.setFont(font)
