# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu PREÇO NORMAL e CONDIÇÃO DE PAGAMENTO:
# - À vista dinheiro/cheque: 10% de desconto
# - À vista no cartão: 5% de desconto
# - Em até 2x no cartão: preço normal
# - 3x ou mais no cartão: 20% de juros 


print('========== LOJAS CODES ==========')

# Solicita ao usuário o valor da compra e converte a entrada para float
preço = float(input('Preço das compras : R$'))

# Mostra as opções de forma de pagamento
print('''FORMAS DE PAGAMENTO
    [ 1 ] à vista dinheiro/cheque
    [ 2 ] à vista cartão
    [ 3 ] 2x no cartão
    [ 4 ] 3x ou mais no cartão''')

# Solicita ao usuário que escolha uma opção de pagamento
opção = int(input('Qual é a opção? '))
print('-=-' * 18)

# Se a opção for 1: aplica 10% de desconto para pagamento à vista em dinheiro ou cheque
if opção == 1:
    desc = preço * (10 / 100)  # Calcula o valor do desconto (10%)
    print(f'Seu compra de R${preço:.2f} vai custar R${preço - desc:.2f} no final.')

# Se a opção for 2: aplica 5% de desconto para pagamento à vista no cartão
elif opção == 2:
    desc = preço * (5 / 100)  # Calcula o valor do desconto (5%)
    print(f'Sua compra de R${preço:.2f} vai custar R${preço - desc:.2f} no final.')

# Se a opção for 3: divide o valor da compra em 2 parcelas sem juros
elif opção == 3:
    parc = preço / 2  # Divide o valor total em 2 parcelas iguais
    print(f'Sua compra de R${preço:.2f} vai custar 2 parcelas de R${parc:.2f}.')  

# Se a opção for 4: aplica 20% de juros e permite o parcelamento em 3x ou mais
elif opção == 4:
    juros = preço + (preço * (20 / 100))  # Adiciona 20% de juros ao valor total
    parcelas = int(input('Em quantas parcelas você deseja pagar? '))  # Pergunta quantas parcelas
    print('-=-' * 18) 
    parc = juros / parcelas  # Divide o valor com juros pelo número de parcelas
    print(f'Sua compra de R${preço:.2f} vai custar R${juros:.2f} no final.')
    print(f'Sua compra será parcelada em {parcelas}x de R${parc:.2f} com JUROS.')

# Caso o usuário digite uma opção inválida
else:
    print('Você não escolheu nenhuma opção valida, tente novamente!')
