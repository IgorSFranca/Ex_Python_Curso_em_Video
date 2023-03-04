print('='*35)
print('{:^35}'.format('BANCO CEV'))
print('='*35)

valor = int(input('Qual o valor você deseja sacar? '))
total = valor
ced = 50
tot_ced = 0

while True:
    if total >= ced:
        total -= ced
        tot_ced += 1
    else: 
        if tot_ced > 0:
          print(f'{tot_ced} cédulas de {ced}')
        if ced == 50:
            ced = 20
        elif ced == 20: 
            ced = 10
        elif ced == 10: 
            ced = 1
        tot_ced = 0
        if total == 0:
          break
print('='*30)
print('Volte Sempre ao BCV')