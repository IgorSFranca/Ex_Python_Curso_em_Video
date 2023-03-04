import math 

print('Vamos calcular o valor do seu empréstimo!')
imovel = float(input('Informe o valor do imóvel: '))
salario = float(input('Informe o valor do seu salário: '))
anos = float(input('Informe em quantos anos você deseja pagar: '))
meses = anos * 12
prestacao = imovel / meses 

if prestacao > (salario * 0.3):
  print('Infelizmente seu empréstimo foi NEGADO devido capacidade de pagamento.')
  print('O valor da parcela é de R$ {:.2f} reais e o máximo permitido é de R$ {:.2f} reais.'.format(prestacao, (salario*0.3)))
else: 
  print('Meus parabéns seu empréstimo foi aprovado.')
  print('O valor da parcela é de R$ {:.2f} reais e o máximo permitido é de R$ {:.2f} reais.'.format(prestacao, (salario*0.3)))
  
# print('\33[1;30;41m Teste \33[m')
# print('\33[1;31;42m Teste \33[m')
# print('\33[1;32;43m Teste \33[m')
# print('\33[1;33;44m Teste \33[m')
# print('\33[1;34;45m Teste \33[m')
# print('\33[1;35;46m Teste \33[m')
# print('\33[1;36;47m Teste \33[m')
