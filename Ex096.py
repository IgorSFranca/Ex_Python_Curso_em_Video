def cabecalho(texto):
    print()
    print(texto)
    print('-'*len(texto))

def calculo_area(l, c):
    area = (l*c)
    print(f'A área de um terreno {l} x {c} é de {area}m².')


cabecalho('Controle de Terrenos')
calculo_area(l = float(input('LARGURA (m): ')), c = float(input('COMPRIMENTO (m): ')))