larg = float(input('Informe a largura da parede: '))
altura = float(input('Informe a altura da parede: '))
area = larg * altura
tinta = area / 2
print('Para pintar {} metros quadrados de parede, serão necessários {} litros de tinta.'.format(area, tinta))