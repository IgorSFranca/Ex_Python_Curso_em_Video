import funcoes_Ex109

preco = float(input('Digite um preço: '))
print(f'A metade de {funcoes_Ex109.moeda(preco)} é {funcoes_Ex109.metade(preco, False)}')
print(f'O dobro de {funcoes_Ex109.moeda(preco)} é {funcoes_Ex109.dobro(preco, True)}')
print(f'Aumentando 10%, temos {funcoes_Ex109.aumento(preco, True)}')