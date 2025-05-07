def aumentar(preço = 0, taxa = 0):
    # Calcula o valor com aumento percentual (por padrão, preço e taxa são 0)
    res = preço + (preço * taxa / 100)
    return res  # Retorna o valor com o aumento aplicado


def diminuir(preço = 0, taxa = 0):
    # Calcula o valor com desconto percentual (por padrão, preço e taxa são 0)
    res = preço - (preço * taxa / 100)
    return res  # Retorna o valor com o desconto aplicado


def dobro(preço = 0):
    # Calcula o dobro do valor (por padrão, preço é 0)
    res = preço * 2
    return res  # Retorna o dobro do valor


def metade(preço = 0):
    # Calcula a metade do valor (por padrão, preço é 0)
    res = preço / 2
    return res  # Retorna a metade do valor


def moeda(preço = 0, moeda = 'R$'):
    # Formata o valor como moeda, com duas casas decimais, vírgula como separador decimal
    # Exemplo: 10.5 → 'R$10,50'
    return f'{moeda}{preço:>.2f}'.replace('.', ',')  # Retorna a string formatada
