import funcoes_Ex108

preco = float(input('Digite um preço: '))
print(f'A metade de R$ {preco:.2f} é {funcoes_Ex108.metade(preco)}')
print(f'O dobro de R$ {preco:.2f} é {funcoes_Ex108.dobro(preco)}')
print(f'Aumentando 10%, temos {funcoes_Ex108.aumento(preco)}')