def aumentar(preço, taxa):
    # Calcula o valor com aumento percentual (ex: aumentar 10%)
    res = preço + (preço * taxa / 100)
    return res  # Retorna o valor final após o aumento


def diminuir(preço, taxa):
    # Calcula o valor com redução percentual (ex: diminuir 10%)
    res = preço - (preço * taxa / 100)
    return res  # Retorna o valor final após a diminuição


def dobro(preço):
    # Calcula o dobro do valor fornecido
    res = preço * 2
    return res  # Retorna o dobro do valor


def metade(preço):
    # Calcula a metade do valor fornecido
    res = preço / 2
    return res  # Retorna a metade do valor
