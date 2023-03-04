from random import randint
print('*'*25)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('*'*25)
cont = 0
while True:
  jogador = int(input('Diga um valor: '))
  play = str(input('Par ou Ímpar? [P/I]: ')).upper().strip()[0]
  computador = randint(0,10)
  soma = jogador + computador
  if soma % 2 == 0:
    if play in 'Pp':
      print(f'Você jogou {jogador} e o computador {computador}. Total deu {soma} que é PAR.')
      print('Você VENCEU!')
      print('Vamos jogar novamente')
      print('*'*25)
      cont += 1
    else:
      print(f'Você jogou {jogador} e o computador {computador}. Total deu {soma} que é PAR.')
      print('Você PERDEU')
      print('*'*25)
      break
  elif soma % 2 == 1:
    if play in 'Ii':
      print(f'Você jogou {jogador} e o computador {computador}. Total deu {soma} que é IMPAR')
      print('Você VENCEU')
      print('Vamos jogar novamente')
      print('*'*25)
      cont += 1
    else: 
      print(f'Você jogou {jogador} e o computador {computador}. Total deu {soma} que é IMPAR.')
      print('Você PERDEU')
      print('*'*25)
      break
print(f'GAME OVER! Você venceu {cont} vezes.')