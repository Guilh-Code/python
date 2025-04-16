# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.     <--- km hd dam m md cm mm -->

v = float(input('Digite um valor em metros: '))
cm = v*100
mm = v*1000
print(f'A medida de {v}m corresponde a {cm}cm e {mm}mm')