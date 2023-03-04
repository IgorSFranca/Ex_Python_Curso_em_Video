sal = float (input('Informe o seu salário: R$ '))
if sal >= 1250: 
  print('O seu salário atualizado é de R$ {:.2f} reais.'.format(sal*1.10))
else:
  print('O seu salário atualizado é de R$ {:.2f} reais.'.format(sal*1.15))