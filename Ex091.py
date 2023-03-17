# Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. 
# Guarde esses resultados em um dicionário. 
# No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.

from random import randint
from time import sleep
from operator import itemgetter

jogadores = {'Jogador_1': randint(1, 6),
             'Jogador_2': randint(1, 6),
             'Jogador_3': randint(1, 6),
             'Jogador_4': randint(1, 6)}
print()
print('VALORES SORTEADOS')
for k, v in jogadores.items():
    sleep(0.8)
    print(f'O {k} tirou {v} no dado.')
print()
print('RANKING')
        # Organizando o Dicionário em ordem Crescente/Decrescente
ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)
for k, v in enumerate(ranking):
    print(f'O {k+1}º Lugar é o {v[0]} com {v[1]} pontos')