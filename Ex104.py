def leiaInt(msg):
    while msg.isnumeric() == False:
        msg = input('Digite um número: ')
        if msg.isnumeric():
            return msg
        else:
            print('\33[1;31;40mERRO! Digite um número inteiro válido\33[m')


n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}')