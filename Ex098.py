from time import sleep

def cont1(texto):
    print(texto)
    for num in range (1, 11):
        print(num, end=' ')
        # sleep(1)
    print('FIM!')

def cont2(texto):
    print(texto)
    for num in range (10, -1, -2):
        print(num, end=' ')
        # sleep(1)
    print('FIM!')

def cont3(texto):
    print(texto)
    for num in range (inicio, fim, passo):
        print(num, end=' ')
    print('FIM!')

def lin():
    print('-='*30)


lin()
cont1('Contagem de 1 até 10 de 1 em 1')
lin()
cont2('Contagem de 10 até 0 de 2 em 2')
lin()
inicio = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
cont3('Agora é sua vez de personalizar a contagem!')
lin()
inicio = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
cont3('Vamos fazer novamente')
lin()