lista = []
resp = cinco =''
cont = 0
while True:
    if resp in 'SsNn':
      lista.append(int(input('Digite um valor: ')))
      cont += 1
      resp = str(input('Deseja continuar? '))
      if resp in 'Nn':
        break
      if 5 in lista: 
         cinco = 'O valor 5 foi encontrado na lista.'
      else: 
         cinco = 'O valor 5 não foi encontrado na lista.'
lista.sort(reverse = True)
print(f'Você digitou {cont} elementos.')
print(f'O valor em Ordem decrescente são {lista}')
print(f'{cinco}')