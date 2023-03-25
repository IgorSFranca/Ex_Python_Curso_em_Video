from time import sleep

def ajuda(texto):
    print('\33[1;30;43m~\33[m'*30)
    print(f'\33[1;30;43m{"SISTEMA DE AJUTA PyHELP":^30}\33[m')
    print('\33[1;30;43m~\33[m'*30)
    while True: 
        fun = str(input(texto))
        if fun == 'fim':
            break
        print('\33[1;30;44m~\33[m'*35)
        print('\33[1;30;44mAcessando o manual do comando {}\33[m'.format(fun))
        print('\33[1;30;44m~\33[m'*35)
        sleep(1)
        help(fun)
        sleep(2)
    return ''

print(ajuda('Função ou Biblioteca: '))