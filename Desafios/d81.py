# Crie um programa que vai ler vários números e colocar em uma lista. Depois disso mostre:
# A) Quantos números foram digitados.                                  
# B) A lista de valores, ordenada de forma decrescente.                                
# C) Se o valor 5 foi digitado e está ou não na lista.


valores = []  # Cria uma lista vazia

while True:  # Loop infinito, até o usuário decidir parar
    num = int(input('Digite um valor: '))  # Lê um número
    valores.append(num)  # Adiciona à lista

    # Pergunta se quer continuar
    resp = str(input('Quer continuar? [S/N]')).upper().strip()  
    if resp != 'S':  # Se a resposta não for S, sai do laço
        break    

print('-=-' * 15)


# Mostra quantos números foram digitados
print(f'Foram digitados {len(valores)} valores na lista')


# Ordena a lista em ordem decrescente e mostra
valores.sort(reverse=True)  # Aqui ordena de forma decrescente
print(f'Os valores em ordem decrescente são {valores}')  # Agora exibe corretamente


# Verifica se o número 5 está na lista
if 5 in valores:
    print('O valor 5 FAZ parte da lista!')
else:
    print('O valor 5 NÃO foi encontrado na lista!')
