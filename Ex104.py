def leiaInt(num):
    while num.isnumeric() != True:
        num = input('Digite um número: ')
        if num.isnumeric() == True:
            return num
        else:
            print('\33[1;31;40mERRO! Digite um número inteiro válido\33[m')


n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}')