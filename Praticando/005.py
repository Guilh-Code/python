#Função que retorna se um número é par
#Retorne True ou False.

def Par_impar(numero):
    if numero % 2 == 0:
        print(f'O numero que você digitou {numero} é PAR')
    else:
        print(f'O numero que você digitou {numero} é IMPAR')


n = int(input('Digite um número: '))
Par_impar(n)
