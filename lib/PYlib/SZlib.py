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
if __name__=="__main__":
    SZShuJu()
    SZGengGaiMiYao('chZnGPGkWfLKZJBBMomh:AtBBZWHdtYlKoMNkNAsI')