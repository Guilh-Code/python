# Dentro do pacote utilidadesCeV que criamos no desafio 111, temos um módulo chamado dado. Crie uma função chamada leiaDinheiro() que seja capaz de funcionar como a função imputa(), mas com uma validação de dados para aceitar apenas valores que seja monetários.


from utilidadesCeV import moeda, dado  # Importa os submódulos 'moeda' e 'dado' de dentro do pacote 'utilidadesCeV'

p = dado.leiaDinheiro('Digite o preço: R$')  # Usa a função 'leiaDinheiro' do módulo 'dado' para ler um valor monetário válido do usuário
moeda.resumo(p, 20, 12)  # Chama a função 'resumo' do módulo 'moeda' passando o preço, aumento de 20% e redução de 12%
