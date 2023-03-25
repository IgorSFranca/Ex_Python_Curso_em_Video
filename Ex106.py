from time import sleep

cores = ('\33[0;',        #0 Sem cor
         '\33[0;30;41m',  #1 Vermelho
         '\33[0;30;42m',  #2 Verde
         '\33[0;30;43m',  #3 Amarelo
         '\33[0;30;44m',  #4 Azul
         '\33[0;30;45m',  #5 Roxo
         '\33[0;30;46m',  #6 Branco
         '\33[m'          #7 Fecha a cor  
         )

def ajuda(texto):
    print(cores[3],'~'*35)
    print(f'{"SISTEMA DE AJUTA PyHELP":^36}')
    print('~'*35,cores[7])
    while True: 
        fun = str(input(texto)).strip()
        if fun.upper() == 'FIM':
            break
        print(cores[4],'~'*40)
        print(f'Acessando o manual do comando \'{fun}\'')
        print('~'*40,cores[7])
        sleep(1)
        print(cores[6], end='')
        help(fun)
        print(cores[7], end='')
        sleep(2)
    return ''

print(ajuda('Função ou Biblioteca: '))