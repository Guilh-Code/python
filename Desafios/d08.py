# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.     <--- km hd dam m md cm mm -->


# Pede ao usuário para digitar um valor em metros e armazena como um número de ponto flutuante
v = float(input('Digite um valor em metros: '))

# Converte o valor de metros para centímetros (1 metro = 100 centímetros)
cm = v * 100

# Converte o valor de metros para milímetros (1 metro = 1000 milímetros)
mm = v * 1000

# Exibe a conversão de metros para centímetros e milímetros, formatando os resultados
print(f'A medida de {v}m corresponde a {cm}cm e {mm}mm')
