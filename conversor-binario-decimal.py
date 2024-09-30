#FEITO POR ANDREI RAMOS LOPES
#https://github.com/Andreirl032

def isExponentialOfTwo(number):
    count=0
    while(number<=2**count):
        if(number==2**count):
            return True
        count+=1
    return False

def decimalBinario(num):
    finalNumber=""
    numberCopy=num
    if(not str(num).isdecimal()):
        return("Erro! O número inserido não é decimal!")
    count=0
    while(numberCopy>=2**(count+1)):
        count+=1
    for i in range(count,-1,-1):
        if(numberCopy>=2**i):
            numberCopy-=2**i
            finalNumber+="1"
        else:
            finalNumber+="0"
    return  f"O número {num} em binário é {finalNumber}"

def binarioDecimal(num):
    strnum=str(num)
    inteiro=0
    count=len(strnum)-1
    for i in strnum:
        if(i!="0" and i!="1"):
            return("Erro! O número inserido não é binário!")
        if(count<0):
            return("Erro!")
        inteiro+=(2**count)*int(i)
        count-=1
    return f"O número {num} em decimal é {inteiro}"

while(True):
    print("CONVERSOR BINÁRIO-DECIMAL")
    opt = int(input("Insira 1 para converter de decimal pra binário, 2 para converter de binário pra decimal, e 3 para encerrar o programa\n"))
    if(opt==1):
        num=int(input("Insira um número inteiro em sistema decimal:\n"))
        print(decimalBinario(num))
    elif(opt==2):
        num=int(input("Insira um número em sistema binário:\n"))
        print(binarioDecimal(num))
    elif(opt==3):
        print("Obrigado por usar o programa! Encerrando...")
        break
    else:
        print("Erro! Código inválido!")