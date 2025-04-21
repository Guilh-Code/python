# Escreva um programa que converta uma temperatura digitada em ºC e converta para ºF.


# Pede ao usuário para informar a temperatura em Celsius e a armazena como um número de ponto flutuante
c = float(input('Informe a temperatura em ºC: '))  

# Converte a temperatura de Celsius para Fahrenheit usando a fórmula:
# Fahrenheit = (Celsius * 9/5) + 32
f = 9 * c / 5 + 32  

# Exibe o resultado da conversão, mostrando a temperatura em Fahrenheit
print(f'A temperatura de {c}ºC corresponde a {f}ºF!.')

