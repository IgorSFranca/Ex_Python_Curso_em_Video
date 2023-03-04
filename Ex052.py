#Um programa que leia um número inteiro e informe se ele é, ou não, um número primo. 

num = int(input('Informe um número: '))
mult = 0
for c in range (1, num+1):
    if num % c == 0:
        mult += 1
if mult == 2:
    print('Este número é PRIMO')
else: 
    print('Este número NÃO É PRIMO')
