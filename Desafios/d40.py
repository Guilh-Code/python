# Crie um programa que leia duas notas de aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
# - Média abaixo de 5.0: REPROVADO
# - Média entre 5.0 e 6.9: RECUPERAÇÃO
# - Média 7.0 ou superior: APROVADO


n1 = float(input('Primeira nota: '))  # Solicita a primeira nota do aluno e converte para float
n2 = float(input('Segunda nota: '))   # Solicita a segunda nota do aluno e converte para float

média = (n1 + n2) / 2  # Calcula a média das duas notas

# Exibe as notas e a média calculada com uma casa decimal
print(f'Tirando {n1} e {n2}, a média do aluno é {média:.1f}')

# Verifica em qual situação o aluno se encontra com base na média
if média >= 5 and média < 7:
    print('Aluno está de RECUPERAÇÃO.')  # Média entre 5 (inclusive) e 7 -> recuperação

elif média < 5:
    print('Aluno está REPROVADO!')  # Média menor que 5 -> reprovado

elif média >= 7:
    print('Aluno está APROVADO!')  # Média 7 ou mais -> aprovado
