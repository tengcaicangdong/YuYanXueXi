import time
import datetime
import os
import re
def FengGeShuJu(a):
    b=a.split('#')
    return b

def QKFanHuiYuYan():
    lujin=os.listdir('shuju')
    lujin.remove('YinPin')
    lujin.remove('she_zhi.txt')
    return lujin

def DanGeShiJianChuoZhuanHuan(ZiFu):
    date_obj=datetime.datetime.strptime(ZiFu, "%Y-%m-%d")
    # 获取时间戳（秒为单位）
    timestamp = date_obj.timestamp()
    return timestamp

def RiQiJinTian():
    timestamp=time.time()
    a=datetime.datetime.fromtimestamp(timestamp)
    formatted_date = a.strftime("%Y-%m-%d")

    return DanGeShiJianChuoZhuanHuan(formatted_date)
    


def DangQianRiQi():  #具体日期
    timestamp=time.time()
    a=datetime.datetime.fromtimestamp(timestamp)
    formatted_date = a.strftime("%Y-%m-%d")
    return formatted_date



def QKJiLu(XieRuShuJu,XieRuDiZhi): 
    with open(f'shuju\\{XieRuDiZhi}',mode='a+',encoding='utf-8') as f:
        f.write(F'\n{XieRuShuJu}')
        f.flush()


def QKBaoCunLuoJi(NeiRong,WenJian): #写入具体内容
    timestamp=str(time.time())
    JuTi=DangQianRiQi()
    WenJian.write(f'{timestamp}#{JuTi}#{NeiRong}')
    WenJian.flush()
    

def QKDuQuRiQi(YuYan,ZhongLei):
    shijian=DangQianRiQi()
    WenJian=open(f'shuju\\{YuYan}\\QK\\{ZhongLei}\\{shijian}.txt',encoding='utf-8',mode='a+')
    return WenJian



def LieBiaoShiJianChuoZhuanHuan(liebiao):
    for i in range(len(liebiao)):
        liebiao[i]=liebiao[i].strip('.txt')

    for i in range(len(liebiao)):
        liebiao[i]=DanGeShiJianChuoZhuanHuan(liebiao[i])

def ZhuanHui(a):
    date_obj = datetime.datetime.fromtimestamp(a)
    date_str = date_obj.strftime("%Y-%m-%d")
    return date_str

def ZhongJianTianShu(da,xiao,liebiao:list):
    while da!=xiao :
        liebiao.append(xiao)
        xiao+=86400


        

def HeBingZiDian(a,b):
    c={}
    for i in a:
        c[i]=[]
    for i in b:
        if i in c:
            pass
        else:
            c[i]=[]
    return c

# def BaoCunShuJu(YuYan):
#     #时间戳#日期#翻译数#单词数
#     jintian=RiQiJinTian()
#     fyliebiao=os.listdir(f'shuju\\{YuYan}\\QK\\FY')
#     dcliebiao=os.listdir(f'shuju\\{YuYan}\\QK\\DC')
#     LieBiaoShiJianChuoZhuanHuan(dcliebiao)#转为时间戳列表
#     LieBiaoShiJianChuoZhuanHuan(fyliebiao)
#     if len(fyliebiao)==2 or 


#     if fymax in dcliebiao:
#         with open(f'shuju\\{YuYan}\\DC\\{ZhuanHui(fymax)}.txt',mode='r+',encoding='utf-8') as f:
#             dczuotian=len(f.readlines())
#     else:
#         dczuotian=0

#     if zuotian in fyliebiao:
#         with open(f'shuju\\{YuYan}\\FY\\{ZhuanHui(zuotian)}.txt',mode='r+',encoding='utf-8') as f:
#             fyzuotian=len(f.readlines())
#     else:
#         fyzuotian=0


#     if zuotian in dcliebiao or zuotian in fyliebiao:
#         with open(f'shuju\\{YuYan}\\XueXiShuJu.txt',mode='r+',encoding='utf-8') as f:
#             f.write(f'{zuotian}#{ZhuanHui(zuotian)}#{fyzuotian}#{dczuotian}')
#             f.flush()
#             print('nihao')

def QKZhongHeRiQi(YuYan): #保存前一天数据
    RiQi=open(f'shuju\\{YuYan}\\XueXiShuJu.txt',mode='r+',encoding='utf-8')
    shuju=RiQi.readlines()
    jintian=RiQiJinTian()

    zuihouRiQi=float(FengGeShuJu(shuju[-1])[0])

    if zuihouRiQi + 86400 == jintian :
        RiQi.close()
        return

    fyliebiao=os.listdir(f'shuju\\{YuYan}\\QK\\FY')
    dcliebiao=os.listdir(f'shuju\\{YuYan}\\QK\\DC')


    LieBiaoShiJianChuoZhuanHuan(dcliebiao)#转为时间戳列表
    LieBiaoShiJianChuoZhuanHuan(fyliebiao)
 
    fymax=max(fyliebiao)
    dcmax=max(dcliebiao)
    
    fykong=[]
    dckong=[]
    
    ZhongJianTianShu(jintian,fymax,fykong)
    ZhongJianTianShu(jintian,dcmax,dckong)
    shujuzidian=HeBingZiDian(fykong,dckong)#所有的日期
# 
    shanchu=[]
    for i in shujuzidian:
        if zuihouRiQi >= i :
            shanchu.append(i)
    for i  in shanchu:
        del shujuzidian[i]
    
    for i in shujuzidian:
        if i in fyliebiao:
            with open(f'shuju\\{YuYan}\\QK\\FY\\{ZhuanHui(i)}.txt',mode='r+',encoding='utf-8') as f:
                shujuzidian[i].append(len(f.readlines()))
        else:
            shujuzidian[i].append(0)

        if i in dcliebiao:
            with open(f'shuju\\{YuYan}\\QK\\DC\\{ZhuanHui(i)}.txt',mode='r+',encoding='utf-8') as f:
                shujuzidian[i].append(len(f.readlines()))
        else:
            shujuzidian[i].append(0)

    for i in shujuzidian:
        RiQi.write(f'{i}#{ZhuanHui(i)}#{shujuzidian[i][0]}#{shujuzidian[i][1]}\n')        

 #时间戳#日期#翻译数#单词数

    RiQi.close()


def quebaoshuju():
    lujin=os.listdir('shuju')
    lujin.remove('YinPin')
    zuotian=ZhuanHui(RiQiJinTian()-86400)
    lujin.remove('she_zhi.txt')
    for i  in lujin:
        fylujin=os.listdir(f'shuju\\{i}\\QK\\FY')
        dclujin=os.listdir(f'shuju\\{i}\\QK\\DC')
        if fylujin==[]:
            with open(f'shuju\\{i}\\QK\\FY\\{zuotian}.txt',mode='w',encoding='utf-8') as f:
                pass
        if dclujin==[]:
            with open(f'shuju\\{i}\\QK\\DC\\{zuotian}.txt',mode='w',encoding='utf-8') as f:
                pass


def QKChuShiPianLi():
    lujin=os.listdir('shuju')
    lujin.remove('YinPin')
    lujin.remove('she_zhi.txt')
    for i in lujin:
        QKZhongHeRiQi(i)
        
def FanHuiShiJianChuo(YuYan):
    with open(f'shuju\\{YuYan}\\XueXiShuJu.txt' ,mode='r',encoding='utf-8') as f:
        shuju=f.readlines()
        shijianchuoshuju=[]
        for i in shuju :
            shijianchuoshuju.append(float(i.split('#')[0]))
        shijianchuoshuju.remove(0.0)
    return shijianchuoshuju
    
def DuiYingShuju(YuYan):
    zidian={}
    with open(f'shuju\\{YuYan}\\XueXiShuJu.txt' ,mode='r',encoding='utf-8') as f:
        shuju=f.readlines()
        for i in shuju :
            a=i.split('#')
            zidian[float(a[0])]=[int(a[2]),int(a[3].strip('\n'))]
    del zidian[0.0]
    return zidian        
    
        

if __name__=='__main__':
    # KQDuQuFYRiQi('RiYu','DC')
    DuiYingShuju('RiYu')
