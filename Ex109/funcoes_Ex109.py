def metade(num=0, sit=True):
    metade = (num/2)
    return metade if sit is False else moeda(num)

def dobro(num=0, sit=True):
    dobro = (num*2)
    return dobro if sit is False else moeda(num)

def aumento(num=0, sit=True):
    aumento = num + (num * 10 / 100)
    return aumento if sit is False else moeda(num)

def moeda(num=0, moeda='R$'):
    return f'{moeda} {num:.2f}'.replace('.',',')