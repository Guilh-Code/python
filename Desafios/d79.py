# Crie um programa onde o usuário possa digitar vários VALORES NÚMERICOS e cadastre-os em uma LISTA. Caso o número já exista lá dentro, ele NÃO SERÁ ADICIONADO. No final, serão exibidos todos os VALORES ÚNICOS digitados, em ORDEM CRESCENTE.


valores = []  # Cria uma lista vazia onde os números únicos serão armazenados

while True:  # Laço infinito que só termina quando o usuário digitar algo diferente de 'S'
    
    num = int(input('Digite um número: '))  # Lê um número do usuário

    # Verifica se o número ainda não está na lista
    if num not in valores:
        valores.append(num)  # Se for novo, adiciona à lista
        print('Valor adicionado com sucesso...')
    else:
        print('Número duplicado! Não vou adicionar...')  # Se já existe, mostra mensagem de duplicata

    # Pergunta se o usuário quer continuar
    resp = str(input('Quer continuar? [S/N]')).upper().strip()[0]

    if resp != 'S':  # Se não for 'S', encerra o laço
        break

valores.sort()  # Ordena a lista em ordem crescente

print(f'Você digitou os valores {valores}')  # Mostra os valores finais, já ordenados
