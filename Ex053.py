frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
print('Você digitou a frase {}.'.format(junto))
inverso = 0
for c in range (len(junto) - 1, -1, -1):
    print(junto[c])