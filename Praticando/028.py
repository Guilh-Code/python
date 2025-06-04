RESET = "\033[0m"
VERDE = "\033[92m"
VERMELHO = "\033[91m"
AZUL = "\033[94m"

def calcular_triangulo(a, b, c):
    
    if (a + b <= c) or (b + c <= a) or (a + c <= b):
        print(f'{VERMELHO}Os lados NÂO formam um triângulo válido!{RESET}')
        print(f'{AZUL}Explicação:{RESET} {VERDE}Um triângulo só existe se a soma de dois lados for maior que o terceiro, para todos os lados.{RESET}')
        
    else:
        print(f'{VERDE}Os lados FORMAM um triângulo válido!{RESET}')
        print('-=-' * 20)
    
        if a == b == c:
            print(f'O triângulo é {VERMELHO}EQUILÁTERO!{RESET}')
            print(f'{AZUL}Explicação:{RESET} {VERDE}Se todos os três lados tiverem a mesma medida ({a} - {b} - {c}), ele é equilátero.{RESET}')

        elif a == b or b == c or a == c:
            print(f'O triângulo é {VERMELHO}ISÓSCELES!{RESET}')
            print(f'{AZUL}Explicação:{RESET} {VERDE}Se dois lados tiverem a mesma medida ({a} - {b} - {c}), ele é isósceles.{RESET}')

        elif a != b and b != c and a != c:
            print(f'O triângulo é {VERMELHO}ESCALENO!{RESET}')
            print(f'{AZUL}Explicação:{RESET} {VERDE}Se todos os três lados tiverem medidas diferentes ({a} - {b} - {c}), ele é escaleno{RESET}')

print('=-=' * 10)
print(f'{AZUL}{'ANALISANDO TRIÂNGULO':^30}{RESET}')
print('=-=' * 10)

l1 = int(input('Digite o primeiro lado: '))
l2 = int(input('Digite o segundo lado: '))
l3 = int(input('Digite o terceiro lado: '))

print('=-=' * 20)

calcular_triangulo(l1, l2, l3)