from random import sample
from time import sleep
print('-'*42)
print('{:^42}'.format('JOGA NA MEGA SENA'))
print('-'*42)
sorteios = int(input('Quantos jogos você quer que eu sorteie? '))
print(f'-=-=-=-=-= Sorteando {sorteios} jogos -=-=-=-=-=')
jogos = []
pos = 0
for sorteio in range (0, sorteios):
  print(f'Jogo {sorteio+1}:', end='')
  sleep(0.5)
  jogadas = sample(range (1, 61), 6)
  jogos.append(jogadas) 
  print(sorted(jogos[pos]))
  pos += 1
print('{:-^42}'.format(' BOA SORTE '))