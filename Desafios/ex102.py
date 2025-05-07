# Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indique o número a calcular e outro chamado show, que será um valor lógico (opcional) indicando se será mostrado ou não na tela o processo de cálculo do fatorial..


# Define a função 'fatorial' que calcula o fatorial de 'n'
# Parâmetro 'show' define se será mostrado o processo (padrão é False)
def fatorial(n, show=False):
    f = 1  # Inicializa a variável que vai armazenar o fatorial

    # Loop de 'n' até 1, decrementando de 1 em 1
    for c in range(n, 0, -1):
        # Se o parâmetro 'show' for True, mostra o processo da multiplicação
        
        if show:
            print(c, end='')  # Imprime o número atual
            
            if c > 1:
                print(' x ', end='')  # Imprime ' x ' entre os números
            else:
                print(' = ', end='')  # Quando chegar no último, imprime ' = '

        f *= c  # Multiplica o valor atual pelo acumulado em 'f'
    return f  # Retorna o resultado do fatorial

# Chama a função com n=5 e show=True, mostrando o processo da multiplicação
print(fatorial(5, show=True))

