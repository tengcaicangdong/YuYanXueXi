import random
import requests

def FYShuJuDuQu(LJ): #返回每一行
    with open(f'shuju\\{LJ}',mode='r',encoding='utf-8') as f:
        YuanShiShuJu=f.readlines()
        random.shuffle(YuanShiShuJu)
    return YuanShiShuJu

def FYShuJuChuLi(YuanShiShuJu,WeiZhi):   
    YuanShiTiMu=YuanShiShuJu[WeiZhi]
    TiMu=YuanShiTiMu.split('#')
    return TiMu

def AIapi_FYShuJu(FYShuJu):
    url='https://spark-api-open.xf-yun.com/v1/chat/completions'
    headers={
        "Content-Type": 'application/json',
        'Authorization': 'Bearer 123456'
    }
    data={
    "model":"generalv3.5",
    "messages": [
        {
            "role": "user",
            "content": "来一个只有程序员能听懂的笑话"
        }
    ],
    "stream":False
}
    res=requests.post()
    pass

def AIapi_DuiHua(FYDuiHua):
    url='https://spark-api-open.xf-yun.com/v1/chat/completions'
    headers={}
    pass
if __name__=='__main__':
    a=FYShuJuDuQu('RiYu//JiLei.txt')
    b=FYShuJuChuLi(a,0)
    print(b)
