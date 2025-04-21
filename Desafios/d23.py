# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados
# Ex: Digite um número: 1834  Unidade: 4    Dezena: 3   Centena: 8   Milhar: 1


num = int(input('Digite um número de 0 a 9999: '))  # Lê um número inteiro de até 4 dígitos

# Calcula o valor de cada casa decimal separadamente:
u = num // 1 % 10      # Unidade: pega o último dígito
d = num // 10 % 10     # Dezena: remove o último dígito e pega o novo último
c = num // 100 % 10    # Centena: remove os dois últimos e pega o novo último
m = num // 1000 % 10   # Milhar: remove os três últimos e pega o novo último

# Mostra o resultado da análise do número
print(f'Analisando o número {num}')
print(f'Unidade: {u}')    # Mostra a unidade
print(f'Dezena: {d}')     # Mostra a dezena
print(f'Centena: {c}')    # Mostra a centena
print(f'Milhar: {m}')     # Mostra o milhar

