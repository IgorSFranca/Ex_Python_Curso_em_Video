def metade(num=0, sit=True):
    metade = (num/2)
    if sit == True:
        return f'R$ {metade:.2f}'.replace('.',',')
    else:
        return metade

def dobro(num=0, sit=True):
    dobro = (num*2)
    if sit == True:
        return f'R$ {dobro:.2f}'.replace('.',',')
    else:
        return dobro

def aumento(num=0, sit=True):
    aumento = num + (num * 10 / 100)
    if sit == True:
        return f'R$ {aumento:.2f}'.replace('.',',')
    else:
        return aumento

def moeda(num=0, moeda='R$'):
    return f'{moeda} {num:.2f}'.replace('.',',')