#Função de saudação
#Crie uma função que receba um nome e imprima: “Olá, [nome]!”


def saudacao(nome):
    print(f'Olá, {nome}')
    


n = str(input('Qual é o seu nome? '))
saudacao(n)