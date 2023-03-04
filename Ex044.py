import math

preco = float(input('Informe o valor do produto: '))
print('Informe a forma de pagamento')
opcao = int(input('''[1] à vista (dinheiro/cheque)
[2] à vista (cartão) 
[3] em até 2x no cartão 
[4] 3x ou mais no cartão 
[ ] Sua opção: '''))
if opcao == 1:
  compra = preco*0.9
elif opcao == 2: 
  compra = preco*0.95
elif opcao == 3: 
  compra = preco
  parc = int(input('Em quantas parcelas deseja fazer? '))
  vlr_parc = compra / parc
  print('O valor de cada parcela será de R$ {} reais.'.format(vlr_parc))
else:
  compra = preco*1.20
  parc = int(input('Em quantas parcelas deseja fazer? '))
  vlr_parc = compra / parc 
  print('O valor de cada parcela será de R$ {} reais.'.format(vlr_parc))
print('O valor da sua compra ficou em R$ {} reais'.format(compra))
