# Adicione o módulo moeda.py criado nos desafios anteriores, uma função chamada resumo(), que mostre na tela algumas informações geradas pelas funções que já temos no módulo criado até aqui.


import moedas  # Importa o módulo 'moedas', que contém funções para manipulação de valores monetários

p = float(input('Digite o preço: R$'))  # Solicita ao usuário que digite um preço e o converte para float
moedas.resumo(p, 20, 12)  # Chama a função 'resumo' do módulo 'moedas', passando o preço (p), aumento de 20% e redução de 12%
