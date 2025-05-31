# Peça dois números e diga qual é o maior, ou se são iguais.

# Exemplo:
# Entrada: 10 e 20
# Saída: O maior número é 20.


n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))

if n1 > n2:
    print(f'O maior número é {n1}')
elif n2 > n1:
    print(f'O maior número é {n2}')
else:
    print('Os dois números são iguais')