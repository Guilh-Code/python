# Faça um programa que leia um número qualquer e mostre o seu fatorial. Exemplo:
# 5! = 5 x 4 x 3 x 2 x 1 = 120


num = int(input('Digite um número para calcular o fatorial: ')) # Lê um número inteiro do usuário

contador = num # Define a variável 'contador' como o número digitado
fatorial = 1 # Inicializa o resultado do fatorial como 1 (neutro da multiplicação)


print(f"{num}! =", end=" ") # Imprime o começo da operação (ex: "5! ="), sem pular linha


# Enquanto o contador for maior que 0, o loop continua
while contador > 0:
    
    # Imprime o número atual (mas com um pequeno erro: o ponto de exclamação aqui está sobrando)
    # Exemplo: 5! x 4! x ... — mas o correto seria só "5 x 4 x ..."
    print(f'{contador}', end=" ")
    
    # Se o número atual for diferente de 1, imprime "x"
    # Se for igual a 1, imprime "=" para finalizar a sequência
    print('x' if contador != 1 else " = ", end=" ")

    
    fatorial *= contador # Multiplica o valor atual do contador no fatorial

    
    contador -= 1 # Diminui o contador em 1 para o próximo passo do laço


print(f'{fatorial}') # Após sair do laço, imprime o resultado final do fatorial

