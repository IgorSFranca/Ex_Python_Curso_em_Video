import math

r1=float(input('Informe a medida da 1 reta: '))
r2=float(input('Informe a medida da 2 reta: '))
r3=float(input('Informe a medida da 3 reta: '))
if(r1+r2)>r3 and (r1+r3)>r2 and (r2+r3)>r1:
  print('As retas informadas PODEM FORMAR TRIÂNGULOS!')
else: 
  print('As retas não forma triângulos!')