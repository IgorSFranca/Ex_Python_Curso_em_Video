jogador = {}
gols = []

jogador ['nome'] = str(input('Nome do Jogador: '))
partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))

print('-'*30)
for partida in range (0, partidas):
    gols.append(int(input(f'Quantos gols fez na partida {partida+1}? ')))
jogador ['gols'] = gols[:]
jogador ['total'] = sum(gols)

print('-'*30)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}.')

print('-'*30)
print(f'O jogador {jogador["nome"]} jogou {partidas} partidas.')
for partida in range (0, partidas):
    print(f'→ Na partida {partida+1}, fez {jogador["gols"][partida]} gols.')
print(f'Foi um total de {jogador["total"]} gols.')
print('-'*30)