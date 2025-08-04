import os

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



if __name__ =='__main__':
    print(SJShuChuShuJu(r'shuju\YingYu\DanCi\jile.txt'))