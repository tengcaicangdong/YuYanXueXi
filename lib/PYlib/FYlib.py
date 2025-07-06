import random
import requests
import os
import json
def FYShuJuDuQu(YuYan,TiKu): #返回每一行
    with open(f'shuju\\{YuYan}\\FanYi\\{TiKu}',mode='r',encoding='utf-8') as f:
        YuanShiShuJu=f.readlines()
        random.shuffle(YuanShiShuJu)
    return YuanShiShuJu

def FYShuJuChuLi(YuanShiShuJu,WeiZhi):   
    YuanShiTiMu=YuanShiShuJu[WeiZhi]
    TiMu=YuanShiTiMu.split('#')
    return TiMu

def AIapi_FYShuJu(FYShuJu,FYTiMu,FYMiYao):
    url="https://spark-api-open.xf-yun.com/v2/chat/completions"
    headers={
        "Content-Type": 'application/json',
        'Authorization': f'Bearer {FYMiYaoJieMi(FYMiYao)}'
    }
    
    data={
        "model": "x1", # 指定请求的模型
        "messages": [
            {
                "role": "user",
                "content": f"题目是这个{FYTiMu},评价一下这个{FYShuJu}翻译的如何。你必须复述一遍的问题在做答"
            }
        ],
        "stream":False
    }
    print(FYTiMu)
    print(FYShuJu)
    res=requests.post(url,headers=headers,json=data)
    res_shuju=json.loads(res.text)
    print(res.status_code)

    return  res_shuju['choices'][0]['message']['content']
    

def AIapi_DuiHua(FYDuiHua,FYMiYao):
    url='https://spark-api-open.xf-yun.com/v2/chat/completions'
    headers={
        "Authorization" :f"Bearer {FYMiYao}",
        "Content-Type": 'application/json'
    }
    body = {
        "model": "x1",
        "user": "user_id",
        "messages": [
        {
            "role": "user",
            "content": FYDuiHua
        }
    ],
        "stream": False,
    }

    res=requests.post(url,headers=headers,json=body,stream= True)
    shuju= json.loads(res.text)
    print(res.status_code)

    return shuju['choices'][0]['message']['content']



def FYMiYaoJieMi(FYMiYao):    
    return FYMiYao
    

def YunYanLieBiao():
    LieBiao=os.listdir('shuju')
    LieBiao.remove('YinPin')
    LieBiao.remove('she_zhi.txt')
    return LieBiao

def FYTiKu(YuYan):
    TikuLieBiao=os.listdir(f'shuju\\{YuYan}\\FanYi')
    return TikuLieBiao



if __name__=='__main__':
    AIapi_DuiHua('nihao','HcrahtUcfiyvtdfmLhni:julQHVYjrzaQyWRSgcYS')
    pass