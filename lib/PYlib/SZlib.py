import os
from sentencex import segment
from pathlib import Path
def SZGengGaiYuYin():
    with open(r'shuju\she_zhi.txt', mode='r',encoding='utf-8') as f:
        duqu=f.readlines()

    with open(r'shuju\she_zhi.txt', mode='w',encoding='utf-8') as f:
        if duqu[0]=='True\n':
            f.write('False\n')

            f.write(duqu[1])
        else:    
            f.write('True'+'\n')
            f.write(duqu[1])

def SZGengGaiMiYao(MiYao):
    with open( 'shuju\\she_zhi.txt',mode='r',encoding='utf-8') as f:
        shuju=f.readline()
    with open('shuju\\she_zhi.txt',mode='w',encoding='utf-8') as f:
        f.write(shuju)
        f.write(MiYao)
        
def SZShuJu():
    shujuwenjian=os.listdir('shuju')
    for i in shujuwenjian:
        if 'she_zhi.txt' in shujuwenjian:
            None
        else:
            with open('shuju\\she_zhi.txt',mode='w',encoding='utf-8')  as f:
                f.write('Flase\n')   


def SZChuangJianYuYan(YuYan):
    if YuYan=='':
        return
    mulu=os.listdir("shuju")
    if YuYan in mulu :
        return
    os.makedirs(f"shuju\\{YuYan}\\DanCi", exist_ok=True)
    os.makedirs(f"shuju\\{YuYan}\\FanYi", exist_ok=True)
    os.makedirs(f"shuju\\{YuYan}\\QK\\DC", exist_ok=True)
    os.makedirs(f"shuju\\{YuYan}\\QK\\FY", exist_ok=True)
    with open(f"shuju\\{YuYan}\\XueXiShuJu.txt",mode='w') as f:
        f.write('0#0#0#0\n')
        pass
    with open(f"shuju\\{YuYan}\\DanCi\\chu_shi_hua.txt",mode='w',encoding='utf-8') as f:
        f.write('什么也没有#什么也没有')
    with open(f"shuju\\{YuYan}\\FanYi\\chu_shi_hua.txt",mode='w',encoding='utf-8') as f:
        f.write('什么也没有#什么也没有')
        

def SZHuoQuYuYan():
    shuju=os.listdir('shuju')
    shuju.remove('YinPin')
    shuju.remove('she_zhi.txt')
    return shuju


def SZQieGe(lujin,YuYan,baocun_lujin):
    with open('dui_ying_yu_yan.txt',mode='r',encoding='utf-8') as a:
        duiying_yuyan=a.readlines()
        duiying_zidian={}

        for i in range(len(duiying_yuyan)):
            duiying_yuyan[i]=duiying_yuyan[i].strip('\n')
            duiying_yuyan[i]=duiying_yuyan[i].split('#')
        for i in duiying_yuyan:
            duiying_zidian[i[0]]=i[1]    
    print(duiying_zidian)

    with open(lujin[0],mode='r',encoding='utf-8') as f:
        shuju=f.read()


    fanhui=list(segment(duiying_zidian[YuYan], shuju))

    for i in range(len(fanhui)) :
        fanhui[i]=fanhui[i].strip('\n')
    fanhui = [w for w in fanhui if w != '']
    print(fanhui)

    with open(baocun_lujin , mode='w',encoding='utf-8'  ) as f:
        for i in fanhui:
            f.write(i+'#'+'None'+'\n')


if __name__=="__main__":
    SZQieGe((r"D:\123.txt",0),'YingYu')