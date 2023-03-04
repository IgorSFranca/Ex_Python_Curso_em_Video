print('\033[1;37;43m~ GERADOR DE PA ~\033[m')
pt = int(input('Primeiro termo: '))
rz = int(input('Razão: '))
termos = int(input('Quantos termos deseja mostrar? '))
pa = pt
print(pa, end=' → ')
while (termos-1) > 0:
    pa += rz
    termos -= 1
    print(pa, end='')
    if (termos-1) > 0:
      print(' → ', end='') 
    else:
      print('')