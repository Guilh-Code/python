# Contar vogais em uma frase
# Conte quantas vogais existem numa frase digitada pelo usuário.


frase = input('Digite uma frase: ')
vogais = 0

for letra in frase:
    if letra in 'aáâãeéiíou':
        vogais += 1

print(f'Tem {vogais} vogais nessa frase.')