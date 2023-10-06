from PyQt5.QtWidgets import QApplication

from cls_new_session_form import cls_new_session_form
from cls_language_option_form import cls_language_option_form
from cls_About_us_form import cls_About_us_form
from cls_key_form import cls_key_form
import sys

app = QApplication([])
# f = clsmainForm()
# f.show()
f2 = cls_language_option_form()
f2.show()

# f3 = cls_new_session_form()
# f3.show()
# f4 = cls_key_form()
# f4.show()
sys.exit(app.exec_())
