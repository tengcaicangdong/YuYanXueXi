import time
import datetime
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

def QKZhongHeRiQi(YuYan):
    RiQi=open(f'shuju\\{YuYan}\\XueXiShuJu.txt',mode='r+',encoding='utf-8')
    shuju=RiQi.readlines()
    if shuju == []:
        return
    zuihou=shuju[-1]

    RiQi.close()
   

if __name__=='__main__':
    # KQDuQuFYRiQi('RiYu','DC')
    QKZhongHeRiQi()