print('~'*22)
print('Sequência de Fibonatti')
print('~'*22)
termos = int(input('Quantos termos deseja mostrar? '))
t1 = 0
t2 = 1
print('~'*22)
print('{} → {}'.format(t1, t2), end='')
cont = 2
while cont < termos:
    t3 = t1 + t2
    print(' → {}'.format(t3), end='')
    t1 = t2
    t2 = t3
    cont += 1