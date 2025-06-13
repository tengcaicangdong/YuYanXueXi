import os
import random


def DCYuanYan():
    shuju=os.listdir('shuju')
    shuju.remove('YinPin')
    shuju.remove('she_zhi.txt')
    return shuju

def DCTuKu(YuYan):
    shuju=os.listdir(f'shuju\\{YuYan}\\DanCi')
    return shuju

def DCDuQuShuJu(DCLuJin):
    with open(f'shuju\\{DCLuJin}',mode='r',encoding='utf-8') as f:
        shuju=f.readlines()
    random.shuffle(shuju)
    return shuju

def DCShuJuChuLi(shuju):
    timu=shuju.split('#')
    return timu

def DCTiMuShuChu(WeiZhi,TiKu:list):
    shuju=random.sample(TiKu,3)
    while  TiKu[WeiZhi] in shuju:
        shuju=random.sample(TiKu,3)
    shuju.append(TiKu[WeiZhi])
    return shuju



if __name__=='__main__':
    a=DCDuQuShuJu('RiYu\\DanCi\\jile.txt')
    print(a)
    print(DCShuJuChuLi(a,2)[0])
    print(DCTiMuShuChu(0,a))
    

