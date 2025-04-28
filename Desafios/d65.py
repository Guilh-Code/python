
# Crie um programa que leia VÁRIOS NÚMEROS inteiros pelo teclado. No final da execução, mostre a MÉDIA ENTRE TODOS os valores e qual foi o MAIOR e o MENOR valores lidos. O programa deve perguntar ao usuário se ele quer ou não CONTINUAR a digitar valores.


# Inicializa as variáveis
resp = 'S'        # Controle de continuidade (inicia como 'S')
media = soma = quant = maior = menor = 0  # Todas as variáveis zeradas

# Enquanto a resposta for 'S', o laço continua
while resp in 'Ss':
    # Solicita um número ao usuário
    num = int(input('Digite um número: '))
    soma += num       # Acumula a soma dos números
    quant += 1        # Conta quantos números foram digitados

    # Se for o primeiro número digitado, define como maior e menor
    if quant == 1:
        maior = menor = num
    else:
        # Atualiza o maior e o menor número se necessário
        if num > maior:
            maior = num
        if num < menor:
            menor = num        
    
    # Pergunta ao usuário se deseja continuar
    resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]

# Calcula a média dos números digitados
media = soma / quant

# Exibe os resultados finais
print(f'A média dos {quant} números digitados foi {media:.2f}')
print(f'O maior número digitado foi {maior} e o menor foi {menor}.')
