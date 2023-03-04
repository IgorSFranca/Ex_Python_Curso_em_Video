reais = float(input('Informe quanto você tem na carteira: '))
conv = reais / 3.27
if conv > 1:
  print('Você possui {:.2f} dolares na carteira.'.format(conv))
else:
  print('Você possui {:.2f} fração de dolar na carteira.'.format(conv))