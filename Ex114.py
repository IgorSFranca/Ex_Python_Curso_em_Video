import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except:
    print('Algo aconteceu. Não é possível acessar o site por este terminal.')
else:
    print('O site está acessível por este terminal.')