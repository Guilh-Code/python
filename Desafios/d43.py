# Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a tabela abaixo: 
# - Abaixo de 18.5: Abaixo do Peso
# - Entre 18.5 e 25: Peso ideal
# - 25 até 30: Sobrepeso
# - 30 até 40: Obesidade
# - Acima de 40: Obesidade mórbida


peso = float(input('Qual é o seu peso? (Kg) '))  # Pergunta o peso da pessoa e converte para float
altura = float(input('Qual é a sua altura (M) '))  # Pergunta a altura da pessoa e converte para float

imc = peso / (altura ** 2)  # Calcula o IMC: peso dividido pela altura ao quadrado
print(f'O IMC dessa pessoa é de {imc:.1f}')  # Mostra o resultado do IMC com uma casa decimal


# Abaixo, o programa avalia o IMC e informa a categoria correspondente:
if imc < 18.5:
    print('Você está ABAIXO DO PESO!')  # IMC menor que 18.5 → abaixo do peso

elif imc <= 25:
    print('Você está no PESO IDEAL!')  # IMC entre 18.5 e 25 → peso ideal

elif imc <= 30:
    print('Você está em SOBREPESO!')  # IMC entre 25 e 30 → sobrepeso

elif imc <= 40:
    print('Você está em OBESIDADE!')  # IMC entre 30 e 40 → obesidade

else:
    print('OBESIDADE MÓRBIDA... cuidado!')  # IMC acima de 40 → obesidade mórbida
