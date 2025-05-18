from PySide6.QtWidgets import QApplication,QWidget,QLabel,QTextEdit,QGridLayout,QPushButton
from lib.PYlib import pyapi
from JieMainui import Ui_Form
from concurrent.futures import ThreadPoolExecutor
class window(QWidget,Ui_Form):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.XianChengChi=ThreadPoolExecutor(25)

        self.FYTiKuWenJianLiBiao=None
        self.FYTiMuWeiZhi=0
        

app=QApplication([])
mywin=window()
mywin.show()
app.exec()

#pyside6-uic JieMain.ui -o JieMainui.py