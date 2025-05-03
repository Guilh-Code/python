# Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.


# Tupla com várias palavras
palavras = (
    'aprender', 'programar', 'linguagem', 'python', 'curso', 'gratis',
    'estudar', 'praticar', 'trabalhar', 'mercado', 'programador', 'futuro'
)

# Loop externo para percorrer cada palavra da tupla
for p in palavras:
    # Mostra a palavra em letras maiúsculas
    print(f'\nNa palavra {p.upper()} temos ', end='')

    # Loop interno para verificar cada letra da palavra
    for letra in p:
        
        # Verifica se a letra é uma vogal (minúscula)
        if letra.lower() in 'aeiou':
            print(letra, end=' ')
