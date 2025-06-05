from PySide6.QtWidgets import QApplication,QWidget
from PySide6.QtCore import QTimer
from lib.PYlib import FYlib
from lib.PYlib import SZlib
from JieMainui import Ui_Form
from concurrent.futures import ThreadPoolExecutor
from playsound import playsound
import asyncio

class window(QWidget,Ui_Form):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('语通智学')
        SZlib.SZShuJu()
        ShiZhi=open('shuju\\she_zhi.txt',mode='r',encoding='utf-8')
        
        self.XieChengChi=asyncio.new_event_loop()
        self.XianChengChi=ThreadPoolExecutor(25)
        self.YunYin=ShiZhi.readline()


        self.FYTiKuWenJianLiBiao=None
        self.FYaiFanHui=None
        self.FYaiFanHui_DH=None
        self.FYWeiZhiBianHua=0
        self.FYTiMuWeiZhi=0
        
        self.FYMiYao=ShiZhi.readline()
        self.FYaiJiShiQi=QTimer()
        self.FYaiJiShiQi_DH=QTimer()
        self.FYYuYan.addItems(FYlib.YunYanLieBiao())
        self.FYTiKu.addItems(FYlib.FYTiKu(self.FYYuYan.currentText()))

        self.FYYuYan.currentTextChanged.connect(self.FYTiKuGengXin)
        self.FYKaiShi.clicked.connect(self.FyKaiShiLuoJi)
        self.FYXiaYiTi.clicked.connect(lambda : self.FYTiMuShangXia(1))
        self.FYShangYiTi.clicked.connect(lambda : self.FYTiMuShangXia(-1))
        self.FYQueRen.clicked.connect(self.FYShuruKuangLuoJi)
        self.FYaiJiShiQi.timeout.connect(self.FYaiFanHuiJianCe)
        self.FYaiQueRen.clicked.connect(self.FYaiDuiHua_DH)
        self.FYaiJiShiQi_DH.timeout.connect(self.FYaiFanHuiJianCe_DH)
        self.FYaiQingKong.clicked.connect(lambda:self.FYaiDuiHuaKuang.setText(' '))


        self.SZYuYingXianShi.setText(self.YunYin)
        self.SZaiMoXingBaoCun.clicked.connect(self.SZaiMoXingMiYao)
        
        ShiZhi.close()
        if self.YunYin=='True\n': 
            playsound('shuju\\YinPin\\ciallo.mp3')


        self.SZYunYing.clicked.connect(lambda: self.SZJMYuYin(SZlib.SZGengGaiYuYin))

    def kong():
        return 

    def FYTiKuGengXin(self):
        self.FYTiKu.clear()
        self.FYTiKu.addItems(FYlib.FYTiKu(self.FYYuYan.currentText()))

    def FyKaiShiLuoJi(self):      
        self.FYTiKuWenJianLiBiao = FYlib.FYShuJuDuQu(self.FYYuYan.currentText(),self.FYTiKu.currentText())
        FYTiMu=FYlib.FYShuJuChuLi(self.FYTiKuWenJianLiBiao,self.FYTiMuWeiZhi)
        self.FYXianShi.setText(f'翻译题目为：{FYTiMu[0]}')
        print(self.FYTiMuWeiZhi)
        print(FYTiMu)


    def FYTiMuShangXia(self,WeiZhiBianDong):
        if self.FYTiKuWenJianLiBiao==None:
            self.FYXianShi.setText(f'还么有加载题库')

        elif WeiZhiBianDong==1:
            if self.FYTiMuWeiZhi+1==len(self.FYTiKuWenJianLiBiao):
                self.FYXianShi.setText(f'已经是最后一题了')
            else:
                self.FYWeiZhiBianHua=1
                self.FYTiMuWeiZhi+=WeiZhiBianDong
                FYTiMu=FYlib.FYShuJuChuLi(self.FYTiKuWenJianLiBiao,self.FYTiMuWeiZhi)
                self.FYXianShi.setText(f'翻译题目为：{FYTiMu[0]}')
                
        else:
            if self.FYTiMuWeiZhi-1==-1:
                self.FYXianShi.setText(f'请下一题')
            else: 
                self.FYWeiZhiBianHua=-1
                self.FYTiMuWeiZhi+=WeiZhiBianDong
                FYTiMu=FYlib.FYShuJuChuLi(self.FYTiKuWenJianLiBiao,self.FYTiMuWeiZhi)
                self.FYXianShi.setText(f'翻译题目为：{FYTiMu[0]}')
                
            
    def FYShuruKuangLuoJi(self):
        self.FYXianShi.setText(self.FYXianShi.text()+'\n'+'你的答案是：'+self.FYShuRu.text())
        self.FYaiDuiHuaKuangluojiFaSong()

    

    def FYaiDuiHuaKuangluojiFaSong(self):
        fa_song=lambda : FYlib.AIapi_FYShuJu(self.FYShuRu.text(),FYlib.FYShuJuChuLi(self.FYTiKuWenJianLiBiao,self.FYTiMuWeiZhi)[0],self.FYMiYao)
        self.FYaiFanHui=self.XianChengChi.submit(fa_song)
        self.FYaiJiShiQi.setInterval(1000)
        self.FYaiJiShiQi.start()
        
    def FYaiFanHuiJianCe(self):
        if self.FYaiFanHui._result!=None:
            self.FYaiDuiHuaKuang.setText(self.FYaiDuiHuaKuang.toPlainText()+'\n'+self.FYaiFanHui._result)
            self.FYaiJiShiQi.stop()

    def FYaiDuiHua_DH(self):
        fa_song=lambda : FYlib.AIapi_DuiHua(self.FYaiShuRu.text(),self.FYMiYao)
        self.FYaiFanHui_DH=self.XianChengChi.submit(fa_song)
        print(type(self.FYaiFanHui_DH))
        self.FYaiJiShiQi_DH.setInterval(1000)
        self.FYaiJiShiQi_DH.start()
    
    def FYaiFanHuiJianCe_DH(self): #对话
        if self.FYaiFanHui_DH._result!=None:
            self.FYaiDuiHuaKuang.setText(self.FYaiDuiHuaKuang.toPlainText()+'\n'+self.FYaiFanHui_DH._result)
            self.FYaiJiShiQi_DH.stop()


    def SZJMYuYin(self,ZX=kong):
        if self.YunYin=='True\n':
            self.SZYuYingXianShi.setText('Flase')
            ZX()
        else:
            self.SZYuYingXianShi.setText('True')
            self.SZYuYingXianShi.setText('True')
            ZX()
    
    def SZaiMoXingMiYao(self):
        MiYao=self.SZaiMoXingShuRu.text()
        self.FYMiYao=MiYao
        SZlib.SZGengGaiMiYao(MiYao)


            
app=QApplication([])
mywin=window()
mywin.show()
app.exec()

#pyside6-uic JieMain.ui -o JieMainui.py