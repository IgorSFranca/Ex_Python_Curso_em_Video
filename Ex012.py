preco = float(input('Informe o preço de um produto: '))
desc = preco * (5/100)
novo_preco = preco - desc 
print('O valor da venda com 5 porcento de desconto é {}.'.format(novo_preco))