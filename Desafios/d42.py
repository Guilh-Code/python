# Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triãngulo será formado:
# - Equilátero: todos os lados iguais
# - Isósceles: dois lados iguais
# - Escaleno: todos os lados diferentes


print('-=-' * 7) 
print('ANALISANDO TRIÂNGULO')  # Exibe o título da análise
print('-=-' * 7) 

# Lê os comprimentos das três retas, convertendo os valores digitados para float
r1 = float(input('Digite o comprimento da primeira reta: '))
r2 = float(input('Digite o comprimento da segunda reta: '))
r3 = float(input('Digite o comprimento da terceira reta: '))

print('-=-' * 7)  # Uma linha de separação visual

# Verifica se as três retas podem formar um triângulo
# Regra do triângulo: a soma de dois lados precisa ser maior que o terceiro lado
if r1 + r2 > r3 and r1 + r3 > r2 and r2 + r3 > r1:
    print('Essas retas podem formar um triângulo ', end='')

    # Verifica se os três lados são iguais
    if r1 == r2 == r3:
        print('EQUILÁTERO!')  # Todos os lados iguais

    # Verifica se todos os lados são diferentes
    elif r1 != r2 != r3 != r1:
        print('ESCALENO!')  # Todos os lados diferentes

    else:
        print('ISÓSCELES!')  # Dois lados iguais e um diferente

else:
    print('Essas retas NÂO PODEM FORMAR um triângulo.')  # Se a condição da soma dos lados não for satisfeita
