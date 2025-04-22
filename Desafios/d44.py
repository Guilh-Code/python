# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu PREÇO NORMAL e CONDIÇÃO DE PAGAMENTO:
# - À vista dinheiro/cheque: 10% de desconto
# - À vista no cartão: 5% de desconto
# - Em até 2x no cartão: preço normal
# - 3x ou mais no cartão: 20% de juros 


print('========== LOJAS CODES ==========')
preço = float(input('Preço das compras : R$'))
print('''FORMAS DE PAGAMENTO
    [ 1 ] à vista dinheiro/cheque
    [ 2 ] à vista cartão
    [ 3 ] 2x no cartão
    [ 4 ] 3x ou mais no cartão''')
opção = int(input('Qual é a opção? '))

if opção == 1:
    desc = preço * (10 / 100)
    print(f'Seu compra de {preço:.2f} vai custar {preço - desc:.2f} no final.')