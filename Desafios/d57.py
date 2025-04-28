# Faça um programa que leia o SEXO de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’. Caso esteja errado, peça a digitação novamente até ter um valor correto.


# Pede para o usuário informar o sexo
# .strip() remove espaços, .upper() transforma em maiúsculo, [0] pega só a primeira letra
sexo = str(input('Informe seu sexo [M/F]: ')).strip().upper()[0]

# Enquanto o sexo digitado não for 'M' nem 'F', repete o pedido
while sexo not in 'MF':
    # Se digitou errado, avisa e pede novamente, aplicando as mesmas correções
    sexo = str(input('Valor inválido! Tente novamente. Informe seu sexo [M/F]: ')).strip().upper()[0]

# Quando o valor for válido, mostra a mensagem de sucesso
print(f'Sexo {sexo} registrado com sucesso!')
