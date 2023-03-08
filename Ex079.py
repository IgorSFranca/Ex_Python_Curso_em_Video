valores = []
resp = 'Ss'
while True:
  if resp in 'Ss':
    valor = int(input('Digite um valor: '))
    if valor not in valores: 
      valores.append(valor)
      print('Valor lançado com sucesso.')
    else: 
      print('Valor duplicado. Não lançado.')
    resp = str(input('Deseja continuar? [S/N]: '))
    while resp not in 'SsNn':
      resp = str(input('Opção não encontrada. Deseja continuar? [S/N]: '))
  else:
    break
print('*'*35)
print(f'Você digitou os valores {valores}')