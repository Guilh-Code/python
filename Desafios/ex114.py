# Crie um código em Python que teste se o site pudim está acessível pelo computador usado.


import urllib  # Importa o módulo urllib (usado para trabalhar com URLs)
import urllib.request  # Importa a sub-biblioteca que permite abrir URLs

try:
    # Tenta abrir o site especificado
    site = urllib.request.urlopen('http://www.pudim.com.br')
except urllib.error.URLError:
    # Se ocorrer erro ao tentar acessar o site (como sem internet ou site fora do ar)
    print('O site Pudim não está acessível no momento.')
else:
    # Se não houver erro, significa que o site está acessível
    print('Consegui acessar o site Pudim com sucesso!')
