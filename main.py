from PySide6.QtWidgets import QApplication,QWidget,QLabel,QTextEdit,QGridLayout,QPushButton
from lib.PYlib import pyapi
from JieMainui import Ui_Form
class window(QWidget,Ui_Form):

    def __init__(self):
        super().__init__()
        self.setupUi(self)


app=QApplication([])
mywin=window()
mywin.show()
app.exec()

#pyside6-uic JieMain.ui -o JieMainui.py