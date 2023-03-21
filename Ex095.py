jogador = {}
ranking = []
gols = []

while True:
  jogador.clear()
  gols.clear()
  total_gol = 0
  jogador['nome'] = str(input('Nome do Jogador: '))
  partida = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
  for c in range (0, partida):
      gol = int(input(f'--→ Quantos gols na partida {c+1}? '))
      total_gol += gol
      gols.append(gol)
      jogador['gols'] = gols[:]
      jogador['total'] = total_gol
  ranking.append(jogador.copy())
  resp = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
  while resp not in 'SN':
    print('Opção não encontrada. Digite somente S ou N.')
    resp = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
  print('-'*30)
  if resp == 'N':
     break
  
print('-'*30)
print(f'{"COD ":<4}{"NOME":<15}{"GOLS":<20}{"TOTAL":<5}')
for i, j in enumerate(ranking):
   print(f'{i:<4}{j["nome"]:<15}{str(j["gols"]):<20}{j["total"]:<5}')
print('-'*30)

while True:
  info = int(input('Mostrar dados de qual jogador? (999 para parar): '))
  print(f'--- Levantamento do jogador {ranking[info]["nome"]}')
  if info == 999:
     break
  for i, dic in enumerate(ranking[info]['gols']):
     print(f'--→ No jogo {i+1} fez {ranking[info]["gols"][i]} gols')
