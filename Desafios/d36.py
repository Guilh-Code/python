# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar o VALOR DA CASA, o SALÁRIO do comprador e em QUANTOS ANOS ele vai pagar.
# Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.


casa = float(input('Valor da casa? R$')) # Pede o valor da casa e converte para float
salario = float(input('Salário do comprador? R$')) # Pede o salário do comprador e converte para float
anos = int(input('Quantos anos de financiamento? ')) # Pede em quantos anos o comprador quer pagar e converte para inteiro

prestação = casa / (anos * 12) # Calcula o valor da prestação mensal (nº total de meses)
minimo = salario * 30 / 100 # Calcula 30% do salário (limite máximo da prestação permitida)

# Mostra o valor da casa, tempo de financiamento e valor da prestação mensal
print(f'Para pagar uma casa de R${casa:.2f} em {anos} a prestação será de R${prestação:.2f}')

# Verifica se a prestação está dentro do limite permitido (30% do salário)
if prestação <= minimo:
    print('Empréstimo pode ser CONCEDIDO!') # Se estiver dentro do limite, aprova o empréstimo
else:
    print('Empréstimo NEGADO!') # Se ultrapassar o limite, nega o empréstimo
    