import math

n1 = float(input('Infome a primeira nota: '))
n2 = float(input('Informe a segunda nota: '))
media = (n1+n2)/2

if media < 5:
  print('REPROVADO')
elif media > 5 and media <7: 
  print('RECUPERAÇÃO')
else:
  print('APROVADO')