# Faça um programa que leia uma frase pelo teclado e mostre:
# 1. Quantas vezes aparece a letra "A".
# 2. Em que posição ela aparece a primeira vez.
# 3. Em que posição ela aparece a última vez.


frase = str(input('Digite uma frase: ')).upper().strip()  
# Pede ao usuário uma frase, transforma tudo em maiúsculas (com .upper()) 
# e remove espaços no início e fim (com .strip())

# Conta quantas vezes a letra 'A' aparece na frase
print(f'A letra A aparece {(frase.count("A"))} vezes na frase.')

# Mostra a posição da primeira vez que a letra 'A' aparece (índice +1 para contar a partir de 1)
print(f'A primeira letra A apareceu na posição {(frase.find("A") + 1)}')

# Mostra a posição da última vez que a letra 'A' aparece (índice +1 para contar a partir de 1)
print(f'A última letra A apareceu na posição {(frase.rfind("A") + 1)}')
