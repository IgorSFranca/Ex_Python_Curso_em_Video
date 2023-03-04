import math

print('VENDAS DE PASSAGENS')
km = float(input('Informe a quantidade de KM que deseja rodar: '))
if km >= 200:
  print('O valor da passagem é de {:.2f} reais.'.format(km * 0.45))
else: 
  print('O valor da passagem é de {:.2f} reais.'.format(km * 0.50))