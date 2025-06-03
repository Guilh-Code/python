nome = str(input('Digite seu nome completo: '))

print('ANALISANDO SEU NOME...')
print('-' * 25)
print(f'Seu nome em maiúsculo é {nome.upper()}.')
print(f'Seu nome em minúsculo é {nome.lower()}.')
print(f'Seu nome tem ao todo {len(nome) - nome.count(' ')}.')

separa = nome.split()

print(f'Seu primeiro nome é {separa[0]} e ele tem {len(separa[0])} letras.')