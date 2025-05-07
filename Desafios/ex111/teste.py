#Crie um pacote chamado utilidadesCeV que tenha dois módulos internos chamados moeda e dado. Transfira todas as funções utilizadas nos desafios 107, 108 e 109 para o primeiro pacote e mantenha tudo funcionando.


from utilidadesCeV import moeda

p = float(input('Digite o preço: R$'))  # Solicita ao usuário que digite um preço e o converte para float
moeda.resumo(p, 20, 12)  # Chama a função 'resumo' do módulo 'moeda', passando o preço (p), aumento de 20% e redução de 12%
