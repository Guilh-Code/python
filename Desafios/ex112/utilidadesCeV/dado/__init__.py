# Função que lê um valor monetário válido digitado pelo usuário
def leiaDinheiro(msg):  
    valido = False  # Variável de controle para o loop de validação
    
    while not valido:  # Continua até que uma entrada válida seja fornecida
        entrada = str(input(msg)).replace(',', '.').strip()  # Lê a entrada, troca vírgula por ponto e remove espaços
        
        if entrada.isalpha() or entrada == '':  # Verifica se a entrada é composta apenas por letras ou está vazia
            print(f'\033[0;31mERRO: \"{entrada}\" é um preço inválido!\033[m')  # Exibe mensagem de erro em vermelho
        else:
            valido = True  # Marca a entrada como válida
            return float(entrada)  # Converte e retorna o valor como float



# Função que garante a leitura de um número inteiro válido
def leiaInt(msg):
    ok = False     # Flag para controle do loop
    valor = 0      # Variável que armazenará o valor inteiro

    # Loop infinito até receber um valor inteiro válido
    while True:
        n = str(input(msg))  # Recebe a entrada do usuário como string

        # Verifica se o que foi digitado é composto apenas por dígitos
        if n.isnumeric():
            valor = int(n)   # Converte para inteiro
            ok = True        # Marca como entrada válida
        else:
            # Mensagem de erro com cor vermelha (ANSI code)
            print('\033[0;31mERRO! Digite um número inteiro válido.\033[m')

        if ok:
            break  # Sai do loop se a entrada for válida
    return valor  # Retorna o número inteiro lido
    