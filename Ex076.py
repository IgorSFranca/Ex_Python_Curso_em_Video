lista_produtos = ('Lápis', 1.75, 
                  'Borracha', 2.00,
                  'Caderno', 15.90,
                  'Estojo', 25.00,
                  'Transferidor', 4.20,
                  'Compasso', 9.99,
                  'Mochila', 120.32,
                  'Canetas', 22.30,
                  'Livro', 34.90)
print('-'*50)
print('{:^50}'.format('LISTAGEM DE PREÇOS'))
print('-'*50)
prod = 0
prec = 1
for produto in lista_produtos:
    if prod < len(lista_produtos):
      print('{:.<40}'.format(lista_produtos[prod]), end='')
      print('R$ {:>7.2f}'.format(lista_produtos[prec]))
      prod += 2
      prec += 2
print('-'*50)


