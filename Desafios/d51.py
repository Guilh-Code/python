# Desenvolva um programa que leia o PRIMEIRO TERMO e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.


primeiro = int(input('Primeiro termo: '))  # Pede ao usuário o primeiro termo da progressão aritmética (PA)
razão = int(input('Razão: '))  # Pede a razão da PA (quanto cada termo aumenta)

décimo = primeiro + (10 - 1) * razão  # Calcula o décimo termo da PA usando a fórmula do termo geral: aₙ = a₁ + (n - 1) * r

for c in range(primeiro, décimo + razão, razão):  # Cria um loop começando no primeiro termo, indo até passar do décimo termo, de razão em razão
    print(f'{c} ', end="-> ")  # Imprime cada termo da PA na mesma linha, com uma seta separando

print('ACABOU')  # Depois de imprimir todos os termos, mostra a mensagem final
