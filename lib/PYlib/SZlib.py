import os

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

if __name__=="__main__":
    SZGengGaiYuYin()