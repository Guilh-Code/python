# Adapte o código do desafio #107, criando uma função adicional chamada moeda() que consiga mostrar os números como um valor monetário formatado.

import moedas  # Importa o módulo 'moedas', que contém funções para manipular valores monetários

p = float(input('Digite o preço: R$'))  
# Solicita ao usuário um valor em reais, e converte a entrada para float

# Exibe a metade do valor formatada como moeda, usando a função 'moeda' para formatação
print(f'A metade de {moedas.moeda(p)} é {moedas.moeda(moedas.metade(p))}')

# Exibe o dobro do valor, também formatado como moeda
print(f'O dobro de {moedas.moeda(p)} é {moedas.moeda(moedas.dobro(p))}')

# Exibe o valor aumentado em 10%, já formatado como moeda
print(f'Aumentando 10%, temos {moedas.moeda(moedas.aumentar(p, 10))}')
