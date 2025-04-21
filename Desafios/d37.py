#  Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a BASE DE CONVERÇÃO: 
# 1 para BINÁRIO
# 2 para OCTAL
# 3 para HEXADECIMAL


num = int(input('Digite um número inteiro: ')) # Pede um número inteiro ao usuário

print('-=-' * 13)
# Mostra as opções de conversão para o usuário
print('''QUAL BASE DE CONVERÇÃO DESEJA 
    [ 1 ] para BINÁRIO
    [ 2 ] para OCTAL 
    [ 3 ] para HEXADECIMAL ''')
opção = int(input('Sua opção: ')) # Lê a opção escolhida e converte para inteiro
print('-=-' * 13)

# Verifica qual opção o usuário escolheu
if opção == 1:
    binario = bin(num)[2:] # Converte o número para binário e remove o prefixo '0b'
    print(f'O número {num} convertido para BINÁRIO é {binario} ')
elif opção == 2:
    octal = oct(num)[2:] # Converte o número para octal e remove o prefixo '0o'
    print(f'O número {num} convertido para OCTAL é {octal}')
elif opção == 3:
    hexa = hex(num)[2:] # Converte o número para hexadecimal e remove o prefixo '0x'
    print(f'O número {num} convertido para HEXADECIMAL é {hexa}')
else:
    print('Você não escolheu nenhuma opcão citada! Tente novamente')     
    # Mensagem de erro caso a opção seja inválida
    