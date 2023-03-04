import math

r1=float(input('Informe a medida da 1 reta: '))
r2=float(input('Informe a medida da 2 reta: '))
r3=float(input('Informe a medida da 3 reta: '))
if(r1+r2)>r3 and (r1+r3)>r2 and (r2+r3)>r1:
  print('As retas informadas PODEM FORMAR TRIÂNGULOS!')
  if r1 == r2 == r3:
    print('Ele forma um triângulo EQUILÁTERO.')
  elif r1 != r2 != r3 != r1:
    print('Ele forma um triângulo ISÓSCELES.')
  else: 
    print('Ele forma um triângulo ESCALENO.')
else: 
  print('As retas não formam triângulos!')