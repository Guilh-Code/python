# Modifique as funções que form criadas no desafio 107 para que elas aceitem um parâmetro a mais, informando se o valor retornado por elas vai ser ou não formatado pela função moeda(), desenvolvida no desafio 108.


import moedas  # Importa o módulo 'moedas' com as funções já atualizadas para aceitar 'formato=True'

p = float(input('Digite o preço: R$'))  
# Recebe o valor inserido pelo usuário e converte para float

print(f'A metade de {moedas.moeda(p)} é {moedas.metade(p, True)}')
# A função 'metade' agora recebe 'formato=True' para retornar o resultado já formatado como moeda

print(f'O dobro de {moedas.moeda(p)} é {moedas.dobro(p, True)}')
# O mesmo vale para a função 'dobro': retorna o valor formatado ao invés de apenas o número

print(f'Aumentando 10%, temos {moedas.aumentar(p, 10, True)}') 
# A função 'aumentar' agora usa 'formato=True' para retornar o valor já formatado como moeda

print(f'Reduzindo 13%, temos {moedas.diminuir(p, 13, True)}')
# A função 'diminuir' também retorna o resultado formatado ao receber 'formato=True'
