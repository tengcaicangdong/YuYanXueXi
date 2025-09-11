import os
from pathlib import Path
def SJYuYanList():
    shuju=os.listdir('shuju')    
    shuju.remove('she_zhi.txt')
    shuju.remove('YinPin')
    return shuju
def SJWenJianList(a,b):
    shuju=os.listdir(f'shuju\\{a}\\{b}') 
    return shuju

def SJShuChuShuJu(LuJin):
    with open(LuJin,mode='r',encoding='utf-8') as f:
        shuju=f.readlines()
        for i in range(len(shuju)):
            shuju[i]=shuju[i].strip('\n')
            shujubiao=[]
        for i in shuju:
            biao=i.split('#')
            shujubiao.append({'题目':biao[0],'答案':biao[1]})
        return shujubiao

def SJXieRuBenDiWenJian(LuJin,shuju_list):
    with open(LuJin,mode='w',encoding='utf-8') as f:
        for  i in shuju_list:
            f.write(f"{i[0]}#{i[1]}\n")

def SJShanChu(lujin,wenjian):
    wenjian_liebiao=os.listdir(lujin)
    if len(wenjian_liebiao) == 1:
        shanchuwenjian=Path(lujin+'\\' + wenjian)
        shanchuwenjian.unlink()
        with open(lujin+'\\' + wenjian,mode='w',encoding='utf-8')  as f:
            f.write('什么也没有#什么也没有')
    else :
        shanchuwenjian=Path(lujin+'\\' + wenjian)
        shanchuwenjian.unlink()




if __name__ =='__main__':
    print(SJShuChuShuJu(r'shuju\YingYu\DanCi\jile.txt'))