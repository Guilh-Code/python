# Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade(). Faça também um programa que importe esse módulo e use algumas dessas funções.


import moedas  # Importa o módulo 'moedas', que contém funções relacionadas a operações com valores monetários

p = float(input('Digite o preço: R$'))  # Solicita ao usuário que digite um preço e converte a entrada para float


# Chama a função 'metade' do módulo 'moedas' passando o preço 'p', e exibe o resultado formatado
print(f'A metade de R${p} é R${moedas.metade(p)}')


# Chama a função 'dobro' do módulo 'moedas' passando o preço 'p', e exibe o resultado formatado
print(f'O dobro de R${p} é R${moedas.dobro(p)}')


# Chama a função 'aumentar' do módulo 'moedas', aumentando o valor em 10%, e exibe o resultado formatado
print(f'Aumentando 10%, temos R${moedas.aumentar(p, 10)}') 
