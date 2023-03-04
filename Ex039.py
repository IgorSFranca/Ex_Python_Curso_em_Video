import math
from datetime import date

ano = int(input('Informe o seu ano de nascimento: '))
idade = date.today().year - ano
print('Hoje você tem {} anos.'.format(idade))
if idade >= 17 and idade < 18:
    print('Chegou o momento de se alistar ao serviço militar.')
elif idade < 17:
  print('Ainda não chegou o momento de se alistar no serviço militar.')
  print('Ainda faltam {} anos para você poder se alistar.'.format(18 - idade))
else: 
  print('Você já passou do prazo de se alistar no serviço militar.')
  print('Você já passou {} anos do prazo de alistamento.'.format(idade - 18))