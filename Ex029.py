import math

print('RADAR')
vel = int(input('Informe a velocidade do carro: '))
if vel >= 80:
  print('Você foi multado!')
  print('A sua multa será de {:.2f} reais.'.format((vel-80)*7))
else:
  print('Parabéns, continue assim.')