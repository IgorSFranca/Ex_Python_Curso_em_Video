def metade(num=0):
    metade = (num/2)
    return metade

def dobro(num=0):
    dobro = (num*2)
    return dobro

def aumento(num=0):
    aumento = num * (num * 10 / 100)
    return aumento

def moeda(num=0, moeda='R$'):
    return f'{moeda} {num:.2f}'.replace('.',',')