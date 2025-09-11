# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'JieMain.ui'
##
## Created by: Qt User Interface Compiler version 6.6.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QGridLayout,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QTabWidget, QTableWidget,
    QTableWidgetItem, QTextEdit, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(831, 537)
        self.verticalLayout_7 = QVBoxLayout(Form)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.tabWidget = QTabWidget(Form)
        self.tabWidget.setObjectName(u"tabWidget")
        self.FanYiJM = QWidget()
        self.FanYiJM.setObjectName(u"FanYiJM")
        self.gridLayout_4 = QGridLayout(self.FanYiJM)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.FYShuRu = QLineEdit(self.FanYiJM)
        self.FYShuRu.setObjectName(u"FYShuRu")

        self.gridLayout_4.addWidget(self.FYShuRu, 5, 0, 1, 1)

        self.FYXiaYiTi = QPushButton(self.FanYiJM)
        self.FYXiaYiTi.setObjectName(u"FYXiaYiTi")

        self.gridLayout_4.addWidget(self.FYXiaYiTi, 3, 0, 1, 1)

        self.FYXianShi = QLabel(self.FanYiJM)
        self.FYXianShi.setObjectName(u"FYXianShi")
        self.FYXianShi.setMinimumSize(QSize(400, 350))
        self.FYXianShi.setStyleSheet(u"border: 2px solid black;\n"
"border-radius: 10px;")
        self.FYXianShi.setWordWrap(True)

        self.gridLayout_4.addWidget(self.FYXianShi, 0, 0, 1, 1)

        self.FYShangYiTi = QPushButton(self.FanYiJM)
        self.FYShangYiTi.setObjectName(u"FYShangYiTi")

        self.gridLayout_4.addWidget(self.FYShangYiTi, 2, 0, 1, 1)

        self.FYTiKu = QComboBox(self.FanYiJM)
        self.FYTiKu.setObjectName(u"FYTiKu")

        self.gridLayout_4.addWidget(self.FYTiKu, 4, 0, 1, 1)

        self.FYYuYan = QComboBox(self.FanYiJM)
        self.FYYuYan.setObjectName(u"FYYuYan")

        self.gridLayout_4.addWidget(self.FYYuYan, 4, 1, 1, 1)

        self.FYQueRen = QPushButton(self.FanYiJM)
        self.FYQueRen.setObjectName(u"FYQueRen")

        self.gridLayout_4.addWidget(self.FYQueRen, 5, 1, 1, 1)

        self.FYaiQueRen = QPushButton(self.FanYiJM)
        self.FYaiQueRen.setObjectName(u"FYaiQueRen")

        self.gridLayout_4.addWidget(self.FYaiQueRen, 5, 4, 1, 1)

        self.FYKaiShi = QPushButton(self.FanYiJM)
        self.FYKaiShi.setObjectName(u"FYKaiShi")

        self.gridLayout_4.addWidget(self.FYKaiShi, 3, 1, 1, 1)

        self.FYaiDuiHuaKuang = QTextEdit(self.FanYiJM)
        self.FYaiDuiHuaKuang.setObjectName(u"FYaiDuiHuaKuang")
        self.FYaiDuiHuaKuang.setMinimumSize(QSize(300, 350))

        self.gridLayout_4.addWidget(self.FYaiDuiHuaKuang, 0, 4, 1, 1)

        self.FYaiQingKong = QPushButton(self.FanYiJM)
        self.FYaiQingKong.setObjectName(u"FYaiQingKong")

        self.gridLayout_4.addWidget(self.FYaiQingKong, 4, 4, 1, 1)

        self.FYaiShuRu = QLineEdit(self.FanYiJM)
        self.FYaiShuRu.setObjectName(u"FYaiShuRu")

        self.gridLayout_4.addWidget(self.FYaiShuRu, 3, 4, 1, 1)

        self.FYAIQiDong = QCheckBox(self.FanYiJM)
        self.FYAIQiDong.setObjectName(u"FYAIQiDong")

        self.gridLayout_4.addWidget(self.FYAIQiDong, 2, 4, 1, 1)

        self.tabWidget.addTab(self.FanYiJM, "")
        self.DanCiJM = QWidget()
        self.DanCiJM.setObjectName(u"DanCiJM")
        self.verticalLayout_4 = QVBoxLayout(self.DanCiJM)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.DCTiMuKuang = QLabel(self.DanCiJM)
        self.DCTiMuKuang.setObjectName(u"DCTiMuKuang")
        self.DCTiMuKuang.setMinimumSize(QSize(350, 220))

        self.horizontalLayout.addWidget(self.DCTiMuKuang)

        self.DCTiKu = QComboBox(self.DanCiJM)
        self.DCTiKu.setObjectName(u"DCTiKu")
        self.DCTiKu.setMinimumSize(QSize(250, 0))

        self.horizontalLayout.addWidget(self.DCTiKu)

        self.DCYuYan = QComboBox(self.DanCiJM)
        self.DCYuYan.setObjectName(u"DCYuYan")

        self.horizontalLayout.addWidget(self.DCYuYan)

        self.DCQueDingTiKu = QPushButton(self.DanCiJM)
        self.DCQueDingTiKu.setObjectName(u"DCQueDingTiKu")

        self.horizontalLayout.addWidget(self.DCQueDingTiKu)


        self.verticalLayout_4.addLayout(self.horizontalLayout)

        self.DCShangYiTi = QPushButton(self.DanCiJM)
        self.DCShangYiTi.setObjectName(u"DCShangYiTi")

        self.verticalLayout_4.addWidget(self.DCShangYiTi)

        self.DCXiaYiTi = QPushButton(self.DanCiJM)
        self.DCXiaYiTi.setObjectName(u"DCXiaYiTi")

        self.verticalLayout_4.addWidget(self.DCXiaYiTi)

        self.DCQueDing = QPushButton(self.DanCiJM)
        self.DCQueDing.setObjectName(u"DCQueDing")

        self.verticalLayout_4.addWidget(self.DCQueDing)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.DCC = QPushButton(self.DanCiJM)
        self.DCC.setObjectName(u"DCC")

        self.gridLayout_2.addWidget(self.DCC, 3, 2, 1, 1)

        self.DCB = QPushButton(self.DanCiJM)
        self.DCB.setObjectName(u"DCB")

        self.gridLayout_2.addWidget(self.DCB, 3, 1, 1, 1)

        self.DCa = QLabel(self.DanCiJM)
        self.DCa.setObjectName(u"DCa")

        self.gridLayout_2.addWidget(self.DCa, 2, 0, 1, 1)

        self.DCb = QLabel(self.DanCiJM)
        self.DCb.setObjectName(u"DCb")

        self.gridLayout_2.addWidget(self.DCb, 2, 1, 1, 1)

        self.DCc = QLabel(self.DanCiJM)
        self.DCc.setObjectName(u"DCc")

        self.gridLayout_2.addWidget(self.DCc, 2, 2, 1, 1)

        self.DCD = QPushButton(self.DanCiJM)
        self.DCD.setObjectName(u"DCD")

        self.gridLayout_2.addWidget(self.DCD, 3, 3, 1, 1)

        self.DCd = QLabel(self.DanCiJM)
        self.DCd.setObjectName(u"DCd")

        self.gridLayout_2.addWidget(self.DCd, 2, 3, 1, 1)

        self.DCA = QPushButton(self.DanCiJM)
        self.DCA.setObjectName(u"DCA")

        self.gridLayout_2.addWidget(self.DCA, 3, 0, 1, 1)


        self.verticalLayout_4.addLayout(self.gridLayout_2)

        self.tabWidget.addTab(self.DanCiJM, "")
        self.XueXiQingKuangJM = QWidget()
        self.XueXiQingKuangJM.setObjectName(u"XueXiQingKuangJM")
        self.gridLayout_8 = QGridLayout(self.XueXiQingKuangJM)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.QKDaoChu = QPushButton(self.XueXiQingKuangJM)
        self.QKDaoChu.setObjectName(u"QKDaoChu")

        self.gridLayout_8.addWidget(self.QKDaoChu, 3, 0, 1, 1)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.QKTianHuiTu = QPushButton(self.XueXiQingKuangJM)
        self.QKTianHuiTu.setObjectName(u"QKTianHuiTu")

        self.horizontalLayout_4.addWidget(self.QKTianHuiTu)

        self.QKZhouHuiTu = QPushButton(self.XueXiQingKuangJM)
        self.QKZhouHuiTu.setObjectName(u"QKZhouHuiTu")

        self.horizontalLayout_4.addWidget(self.QKZhouHuiTu)

        self.QKYueHuiTu = QPushButton(self.XueXiQingKuangJM)
        self.QKYueHuiTu.setObjectName(u"QKYueHuiTu")

        self.horizontalLayout_4.addWidget(self.QKYueHuiTu)

        self.QKYuYan = QComboBox(self.XueXiQingKuangJM)
        self.QKYuYan.setObjectName(u"QKYuYan")

        self.horizontalLayout_4.addWidget(self.QKYuYan)


        self.gridLayout_8.addLayout(self.horizontalLayout_4, 2, 0, 1, 1)

        self.QKHuiTuZhuangTai = QLabel(self.XueXiQingKuangJM)
        self.QKHuiTuZhuangTai.setObjectName(u"QKHuiTuZhuangTai")

        self.gridLayout_8.addWidget(self.QKHuiTuZhuangTai, 1, 0, 1, 1)

        self.KQTuiTuChuangKuo = QWidget(self.XueXiQingKuangJM)
        self.KQTuiTuChuangKuo.setObjectName(u"KQTuiTuChuangKuo")
        self.KQTuiTuChuangKuo.setMinimumSize(QSize(350, 300))
        self.horizontalLayout_6 = QHBoxLayout(self.KQTuiTuChuangKuo)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.QKTuiTuBuJu = QHBoxLayout()
        self.QKTuiTuBuJu.setObjectName(u"QKTuiTuBuJu")

        self.horizontalLayout_6.addLayout(self.QKTuiTuBuJu)


        self.gridLayout_8.addWidget(self.KQTuiTuChuangKuo, 0, 0, 1, 1)

        self.tabWidget.addTab(self.XueXiQingKuangJM, "")
        self.ShuJuSheZhiJM = QWidget()
        self.ShuJuSheZhiJM.setObjectName(u"ShuJuSheZhiJM")
        self.gridLayout_6 = QGridLayout(self.ShuJuSheZhiJM)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_5 = QGridLayout()
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.SJBiao = QTableWidget(self.ShuJuSheZhiJM)
        if (self.SJBiao.columnCount() < 4):
            self.SJBiao.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.SJBiao.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.SJBiao.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.SJBiao.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.SJBiao.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.SJBiao.setObjectName(u"SJBiao")

        self.verticalLayout_5.addWidget(self.SJBiao)

        self.SJYuYan = QComboBox(self.ShuJuSheZhiJM)
        self.SJYuYan.setObjectName(u"SJYuYan")
        self.SJYuYan.setMinimumSize(QSize(200, 0))

        self.verticalLayout_5.addWidget(self.SJYuYan)

        self.SJZhongLei = QComboBox(self.ShuJuSheZhiJM)
        self.SJZhongLei.setObjectName(u"SJZhongLei")

        self.verticalLayout_5.addWidget(self.SJZhongLei)

        self.SJWenJian = QComboBox(self.ShuJuSheZhiJM)
        self.SJWenJian.setObjectName(u"SJWenJian")

        self.verticalLayout_5.addWidget(self.SJWenJian)

        self.SJQueDing = QPushButton(self.ShuJuSheZhiJM)
        self.SJQueDing.setObjectName(u"SJQueDing")

        self.verticalLayout_5.addWidget(self.SJQueDing)

        self.SJShanChuAnNiu = QPushButton(self.ShuJuSheZhiJM)
        self.SJShanChuAnNiu.setObjectName(u"SJShanChuAnNiu")

        self.verticalLayout_5.addWidget(self.SJShanChuAnNiu)

        self.SJBaoCun = QPushButton(self.ShuJuSheZhiJM)
        self.SJBaoCun.setObjectName(u"SJBaoCun")

        self.verticalLayout_5.addWidget(self.SJBaoCun)


        self.gridLayout_5.addLayout(self.verticalLayout_5, 0, 0, 1, 1)


        self.gridLayout_6.addLayout(self.gridLayout_5, 0, 0, 1, 1)

        self.tabWidget.addTab(self.ShuJuSheZhiJM, "")
        self.ChengXuSheZhiJM = QWidget()
        self.ChengXuSheZhiJM.setObjectName(u"ChengXuSheZhiJM")
        self.verticalLayout_6 = QVBoxLayout(self.ChengXuSheZhiJM)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.widget = QWidget(self.ChengXuSheZhiJM)
        self.widget.setObjectName(u"widget")
        self.gridLayout_10 = QGridLayout(self.widget)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.gridLayout_9 = QGridLayout()
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.SZWenJianZhuangTai = QLabel(self.widget)
        self.SZWenJianZhuangTai.setObjectName(u"SZWenJianZhuangTai")
        self.SZWenJianZhuangTai.setMinimumSize(QSize(0, 100))

        self.horizontalLayout_3.addWidget(self.SZWenJianZhuangTai)

        self.SZXuanZeWenJian = QPushButton(self.widget)
        self.SZXuanZeWenJian.setObjectName(u"SZXuanZeWenJian")

        self.horizontalLayout_3.addWidget(self.SZXuanZeWenJian)

        self.SJKaiFenGeAnNiu = QPushButton(self.widget)
        self.SJKaiFenGeAnNiu.setObjectName(u"SJKaiFenGeAnNiu")

        self.horizontalLayout_3.addWidget(self.SJKaiFenGeAnNiu)

        self.SZFenGeYuYan = QComboBox(self.widget)
        self.SZFenGeYuYan.setObjectName(u"SZFenGeYuYan")

        self.horizontalLayout_3.addWidget(self.SZFenGeYuYan)

        self.SZFenGeZhongLei = QComboBox(self.widget)
        self.SZFenGeZhongLei.setObjectName(u"SZFenGeZhongLei")

        self.horizontalLayout_3.addWidget(self.SZFenGeZhongLei)


        self.gridLayout_9.addLayout(self.horizontalLayout_3, 0, 1, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.SZYuYingXianShi = QLabel(self.widget)
        self.SZYuYingXianShi.setObjectName(u"SZYuYingXianShi")
        self.SZYuYingXianShi.setMinimumSize(QSize(0, 100))

        self.horizontalLayout_2.addWidget(self.SZYuYingXianShi)

        self.SZYunYing = QPushButton(self.widget)
        self.SZYunYing.setObjectName(u"SZYunYing")

        self.horizontalLayout_2.addWidget(self.SZYunYing)


        self.gridLayout_9.addLayout(self.horizontalLayout_2, 3, 1, 1, 1)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.SZaiMoXing = QLabel(self.widget)
        self.SZaiMoXing.setObjectName(u"SZaiMoXing")

        self.verticalLayout_3.addWidget(self.SZaiMoXing)

        self.SZaiMoXingShuRu = QLineEdit(self.widget)
        self.SZaiMoXingShuRu.setObjectName(u"SZaiMoXingShuRu")

        self.verticalLayout_3.addWidget(self.SZaiMoXingShuRu)

        self.SZaiMoXingBaoCun = QPushButton(self.widget)
        self.SZaiMoXingBaoCun.setObjectName(u"SZaiMoXingBaoCun")

        self.verticalLayout_3.addWidget(self.SZaiMoXingBaoCun)

        self.pushButton_4 = QPushButton(self.widget)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.verticalLayout_3.addWidget(self.pushButton_4)


        self.gridLayout_9.addLayout(self.verticalLayout_3, 2, 1, 1, 1)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.SZChuangJianYuYan = QLabel(self.widget)
        self.SZChuangJianYuYan.setObjectName(u"SZChuangJianYuYan")

        self.verticalLayout.addWidget(self.SZChuangJianYuYan)

        self.SZChuangJianYuYanShuRu = QLineEdit(self.widget)
        self.SZChuangJianYuYanShuRu.setObjectName(u"SZChuangJianYuYanShuRu")

        self.verticalLayout.addWidget(self.SZChuangJianYuYanShuRu)

        self.SZChuangJianYuYanQueDing = QPushButton(self.widget)
        self.SZChuangJianYuYanQueDing.setObjectName(u"SZChuangJianYuYanQueDing")

        self.verticalLayout.addWidget(self.SZChuangJianYuYanQueDing)


        self.gridLayout_9.addLayout(self.verticalLayout, 1, 1, 1, 1)


        self.gridLayout_10.addLayout(self.gridLayout_9, 0, 0, 1, 1)


        self.verticalLayout_2.addWidget(self.widget)


        self.verticalLayout_6.addLayout(self.verticalLayout_2)

        self.tabWidget.addTab(self.ChengXuSheZhiJM, "")

        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)


        self.verticalLayout_7.addLayout(self.gridLayout)


        self.retranslateUi(Form)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.FYXiaYiTi.setText(QCoreApplication.translate("Form", u"\u4e0b\u4e00\u9898", None))
        self.FYXianShi.setText(QCoreApplication.translate("Form", u"\u7b49\u5f85\u4e2d", None))
        self.FYShangYiTi.setText(QCoreApplication.translate("Form", u"\u4e0a\u4e00\u9898", None))
        self.FYQueRen.setText(QCoreApplication.translate("Form", u"\u786e\u8ba4", None))
        self.FYaiQueRen.setText(QCoreApplication.translate("Form", u"\u786e\u8ba4", None))
        self.FYKaiShi.setText(QCoreApplication.translate("Form", u"\u786e\u8ba4\u9898\u5e93", None))
        self.FYaiQingKong.setText(QCoreApplication.translate("Form", u"\u6e05\u7a7a", None))
        self.FYAIQiDong.setText(QCoreApplication.translate("Form", u"\u662f\u5426\u542f\u7528", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.FanYiJM), QCoreApplication.translate("Form", u"\u7ffb\u8bd1", None))
        self.DCTiMuKuang.setText(QCoreApplication.translate("Form", u"\u7b49\u5f85\u4e2d", None))
        self.DCQueDingTiKu.setText(QCoreApplication.translate("Form", u"\u786e\u5b9a\u9898\u5e93", None))
        self.DCShangYiTi.setText(QCoreApplication.translate("Form", u"\u4e0a\u4e00\u9898", None))
        self.DCXiaYiTi.setText(QCoreApplication.translate("Form", u"\u4e0b\u4e00\u9898", None))
        self.DCQueDing.setText(QCoreApplication.translate("Form", u"\u786e\u5b9a", None))
        self.DCC.setText(QCoreApplication.translate("Form", u"c", None))
        self.DCB.setText(QCoreApplication.translate("Form", u"b", None))
        self.DCa.setText(QCoreApplication.translate("Form", u"\u9009\u9879a", None))
        self.DCb.setText(QCoreApplication.translate("Form", u"\u9009\u9879b", None))
        self.DCc.setText(QCoreApplication.translate("Form", u"\u9009\u9879c", None))
        self.DCD.setText(QCoreApplication.translate("Form", u"d", None))
        self.DCd.setText(QCoreApplication.translate("Form", u"\u9009\u9879d", None))
        self.DCA.setText(QCoreApplication.translate("Form", u"a", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.DanCiJM), QCoreApplication.translate("Form", u"\u5355\u8bcd", None))
        self.QKDaoChu.setText(QCoreApplication.translate("Form", u"\u5bfc\u51fa", None))
        self.QKTianHuiTu.setText(QCoreApplication.translate("Form", u"\u6309\u5929\u7ed8\u56fe", None))
        self.QKZhouHuiTu.setText(QCoreApplication.translate("Form", u"\u6309\u5468\u7ed8\u56fe", None))
        self.QKYueHuiTu.setText(QCoreApplication.translate("Form", u"\u6309\u6708\u7ed8\u56fe", None))
        self.QKHuiTuZhuangTai.setText(QCoreApplication.translate("Form", u"\u72b6\u6001\u663e\u793a", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.XueXiQingKuangJM), QCoreApplication.translate("Form", u"\u5b66\u4e60\u60c5\u51b5", None))
        ___qtablewidgetitem = self.SJBiao.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"\u65b0\u5efa\u5217", None));
        ___qtablewidgetitem1 = self.SJBiao.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"\u65b0\u5efa\u5217", None));
        ___qtablewidgetitem2 = self.SJBiao.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Form", u"\u65b0\u5efa\u5217", None));
        ___qtablewidgetitem3 = self.SJBiao.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Form", u"\u65b0\u5efa\u5217", None));
        self.SJQueDing.setText(QCoreApplication.translate("Form", u"\u786e\u5b9a", None))
        self.SJShanChuAnNiu.setText(QCoreApplication.translate("Form", u"\u5220\u9664", None))
        self.SJBaoCun.setText(QCoreApplication.translate("Form", u"\u4fdd\u5b58", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.ShuJuSheZhiJM), QCoreApplication.translate("Form", u"\u6570\u636e\u8bbe\u7f6e", None))
        self.SZWenJianZhuangTai.setText(QCoreApplication.translate("Form", u"<html><head/><body><p>\u9009\u62e9\u7684txt\u6587\u4ef6___\u4fdd\u5b58\u7684\u5730\u65b9      </p><p>\u72b6\u6001\uff1a\u7b49\u5f85\u4e2d</p></body></html>", None))
        self.SZXuanZeWenJian.setText(QCoreApplication.translate("Form", u"\u9009\u62e9\u6587\u4ef6", None))
        self.SJKaiFenGeAnNiu.setText(QCoreApplication.translate("Form", u"\u5f00\u59cb", None))
        self.SZYuYingXianShi.setText(QCoreApplication.translate("Form", u"\u72b6\u6001\u663e\u793a", None))
        self.SZYunYing.setText(QCoreApplication.translate("Form", u"\u542f\u52a8\u8bed\u97f3\u5f00\u5173", None))
        self.SZaiMoXing.setText(QCoreApplication.translate("Form", u"\u72b6\u6001\u663e\u793a", None))
        self.SZaiMoXingShuRu.setText("")
        self.SZaiMoXingBaoCun.setText(QCoreApplication.translate("Form", u"\u4fdd\u5b58", None))
        self.pushButton_4.setText(QCoreApplication.translate("Form", u"\u7b49\u5f85", None))
        self.SZChuangJianYuYan.setText(QCoreApplication.translate("Form", u"\u521b\u5efa\u65b0\u7684\u8bed\u8a00", None))
        self.SZChuangJianYuYanQueDing.setText(QCoreApplication.translate("Form", u"\u786e\u5b9a", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.ChengXuSheZhiJM), QCoreApplication.translate("Form", u"\u7a0b\u5e8f\u8bbe\u7f6e", None))
    # retranslateUi

