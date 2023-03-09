pares = []
impares = []
lista = [] 
num = 0
resp =''
while True: 
    if resp in 'Ss':
      num = int(input('Digite um número: '))
      resp = str(input('Deseja Continuar? ')).strip()[0]
      lista.append(num)
      if num % 2 == 0:
         pares.append(num)
      else:
         impares.append(num)
    else:
        break
print('*'*35)
print(f'A lista completa é {lista}')
print(f'A lista de pares é {pares}')
print(f'A lista de ímpares é {impares}')