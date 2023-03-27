def leiaInt(texto):
    while True:
      try:
        n = int(input(texto))
      except ValueError:
        print(cores['vermelho'],'Erro! Digite um número inteiro válido', cores['fechar'])
        continue
      except KeyboardInterrupt:
        print(cores['vermelho'],'Erro! O usuário escolheu por encerrar o programa.', cores['fechar'])
        return 0
      else:
        return n

def leiaReal(texto):
    while True:
      try:
        n = float(input(texto))
      except ValueError:
        print(cores['vermelho'],'Erro! Digite um número inteiro válido', cores['fechar'])
        continue
      except KeyboardInterrupt:
        print(cores['vermelho'],'Erro! O usuário escolheu por encerrar o programa.', cores['fechar'])
        return 0
      else: 
        return n

cores = {'vermelho':'\33[31m',
         'fechar':'\33[m'}