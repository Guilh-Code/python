# Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.


nome = str(input('Qual é o seu nome completo: '))  # Pede o nome completo do usuário

# Verifica se a palavra "SILVA" está presente no nome (sem considerar maiúsculas/minúsculas)
# Usa .upper() para garantir que a comparação seja feita em letras maiúsculas
print(f'Seu nome tem Silva? {("SILVA" in nome.upper())}')

