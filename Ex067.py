cont = 1
while True:
  valor = int(input('Quer ver a tabuada de qual valor? '))
  print('-'*40)
  if valor < 0:
    break
  while cont < 11:
    print(f'''{valor} x {cont} = {valor*cont}''')
    cont += 1
  print('-'*40)
  cont = 1
print('Programa finalizado')