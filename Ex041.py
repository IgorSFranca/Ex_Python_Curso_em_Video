import math
from datetime import date

ano = int(input('Informe o ano de nascimento do atleta: '))
idade = date.today().year - ano

if idade <= 9: 
  print('MIRIM')
elif idade <= 14: 
  print('INFANTIL')
elif idade <= 19:
  print('JUNIOR')
elif idade <= 25: 
  print('SÊNIOR')
else: 
  print('MASTER')