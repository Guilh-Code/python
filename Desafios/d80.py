# Crie um programa onde o usuário possa digitar cinco VALORES NÚMERICOS e cadastre-os em uma LISTA, JÁ NA POSIÇÃO CORRETA de inserção (sem usar o SORT()). No final, mostre a LISTA ORDENADA na tela.


lista = []  # Cria uma lista vazia onde os números serão inseridos em ordem

for c in range(0, 5):  # Um laço que se repete 5 vezes (de 0 até 4)
    num = int(input('Digite um número: '))  # Lê um número digitado pelo usuário e converte para inteiro

    # Se a lista estiver vazia ou o número for maior que o último da lista
    if not lista or num > lista[-1]:
        lista.append(num)  # Adiciona o número ao final da lista

    else:
        pos = 0  # Variável de posição começa em 0

        # Enquanto a posição for menor que o tamanho da lista
        while pos < len(lista):
            # Se o número digitado for menor ou igual ao número na posição atual
            if num <= lista[pos]:
                lista.insert(pos, num)  # Insere o número na posição correta (antes de um número maior ou igual)
                break  # Sai do laço porque o número já foi inserido
            pos += 1  # Avança para a próxima posição da lista

print(lista)  # Exibe a lista final com os números ordenados
   