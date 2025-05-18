import random
from datetime import datetime
import time

def DuQuWenJian(a):
    b=open(f'shuju\RiYu\\{a}',mode='r',encoding='utf-8')
    c=b.readlines()
    b.close()
    return c


def ChuLiShuJu(a):
    b=random.choice(a)
    c=b.split('#')
    return c


def LiShiTianJia(a):
    c=open(f'shuju\RiYu\\{str(datetime.now())[0:10]}.txt',mode='a')
    c.write(f'{a}')
    c.close()


def ShuJuTianJia(a,b,c='JiLei.txt'):
    d=open(f'shuju\RiYu\\{c}',mode='a+',encoding='utf-8')
    d.seek(0)
    f=d.readlines()
    d.write(f'\n{a}#{b}#0#{str(datetime.now())[0:10]}#{len(f)}')
    d.close()


if __name__ == '__main__' :
    QiDong='k'
    while QiDong=='k':
        pp=input('输入选项：1.关闭程序 2.默写 3.添加\n你的选择：')
        if pp=='1':
            print('关闭')
            QiDong='l'
        elif pp=='2':
            ll=DuQuWenJian('JiLei.txt')
            jj=ChuLiShuJu(ll)
            print(jj[0])
            input('你的答案：')
            print(jj[1])
            time.sleep(2)
        else:
            ShuRuRiRu=input('你要添加的日语：')
            ShuRuZhongWen=input('中文答案：')
            ShuJuTianJia(ShuRuRiRu,ShuRuZhongWen)
            print('已添加')
