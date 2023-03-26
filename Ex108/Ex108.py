import funcoes_Ex108

preco = float(input('Digite um preço: '))
print(f'A metade de {funcoes_Ex108.moeda(preco)} é {funcoes_Ex108.moeda(funcoes_Ex108.metade(preco))}')
print(f'O dobro de {funcoes_Ex108.moeda(preco)} é {funcoes_Ex108.moeda(funcoes_Ex108.dobro(preco))}')
print(f'Aumentando 10%, temos {funcoes_Ex108.moeda(funcoes_Ex108.aumento(preco))}')