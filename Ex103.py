def ficha(jogador='', gols=0):
    if jogador == '':
        jogador = '<desconhecido>'
    # if gols :
    #     gols = 0
    return f'O jogador {jogador} fez {gols} gol(s) no campeonato.'

jogador = str(input('Nome do Jogador: '))
gols = int(input('Número de gols: '))
print(ficha(jogador, gols))