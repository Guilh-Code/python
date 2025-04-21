# Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO.


from datetime import date # Importa o módulo para trabalhar com datas
ano = int(input('Digite um ano, Coloque 0 para analisar o ano atual: ')) # Pede ao usuário um ano, ou 0 para usar o ano atual

if ano == 0:
    ano = date.today().year # Se o usuário digitou 0, pega o ano atual do sistema

# Verifica se o ano é bissexto:
# - divisível por 4 e não por 100, OU divisível por 400
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'O ano {ano} É BISSEXTO') # Se for, exibe que o ano é bissexto
else:
    print(f'O ano {ano} NÂO é BISSEXTO') # Caso contrário, diz que não é bissexto
    