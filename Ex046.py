from time import sleep

print('-*'*10)
print('Vamos a contagem regressiva!')
for c in range (10, -1, -1):
    sleep(1)
    print(c)
print('BOOM!')
print('-*'*10)