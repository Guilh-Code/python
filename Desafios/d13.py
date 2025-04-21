# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.


# Pede ao usuário o salário do funcionário e armazena como um número de ponto flutuante
s = float(input('Qual é o salário do Funcionário: R$'))  

# Calcula o novo salário aplicando um aumento de 15% (s * 0.15)
novo = s + (s * 15 / 100)  

# Alternativamente, você poderia usar a fórmula: novo = s * 1.15 para aplicar diretamente o aumento de 15%

# Exibe o novo salário após o aumento de 15%, formatando o valor com 2 casas decimais
print(f'Um funcionário que ganhava R${s}, com 15% de aumento, passa a receber R${novo:.2f}')

