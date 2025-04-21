# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.   Ex: Ana Maria de Souza     primeiro = Ana    último = Souza


nome = str(input('Digite seu nome completo: ')).strip() # Pede o nome completo e remove espaços extras no início e no fim

n = nome.split()  # Divide o nome em partes, separando por espaços e criando uma lista com cada palavra

print('Muito prazer em te conhecer!')  # Mensagem de boas-vindas

print(f'Seu primeiro nome é {(n[0])}')  # Mostra o primeiro nome (índice 0 da lista)
print(f'Seu último nome é {(n[len(n)-1])}')  # Mostra o último nome (último índice da lista, usando len - 1)
