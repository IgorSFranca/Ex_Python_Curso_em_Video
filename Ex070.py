print('-'*25)
print('{:^25}'.format('LOJA SUPER BARATÃO'))
print('-'*25)
compras = alta = m_preco = cont = 0
continua = m_produto = ' '
while True:
  produto = str(input('Nome do produto: '))
  preco = float(input('Preço: R$ '))
  compras += preco
  cont += 1
  if preco > 1000:
    alta += 1
  if cont == 1:
    m_preco = preco
    m_produto = produto
  else: 
    if preco < m_preco: 
      m_preco = preco
      m_produto = produto
  continua = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
  while continua not in 'SN':
    continua = str(input('Opção não encontrada. Deseja continuar? [S/N] ')).upper().strip()[0]
  if continua == 'N':
    break
print('{:-^40}'.format(' FIM DO PROGRAMA '))
print(f'O total da compra foi de R$ {compras:.2f} reais.')
print(f'Temos {alta} produtos custando mais de R$ 1.000,00')
print(f'O produto mais barato foi {m_produto} que custou R$ {m_preco:.2f} reais')

