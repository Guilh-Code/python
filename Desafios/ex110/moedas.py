def aumentar(preço = 0, taxa = 0, formato=False):
    res = preço + (preço * taxa/100)
    return res if formato == False else moeda(res)  
    # Se formato=False, retorna o valor numérico
    # Se formato=True, formata o resultado como moeda antes de retornar

def diminuir(preço = 0, taxa = 0, formato=False):
    res = preço - (preço * taxa/100)
    return res if formato == False else moeda(res)  
    # Mesma lógica: retorna o valor numérico ou formatado conforme 'formato'

def dobro(preço = 0, formato=False):
    res = preço * 2
    return res if formato == False else moeda(res)  
    # Agora também pode retornar o dobro formatado como moeda

def metade(preço = 0, formato=False):
    res = preço / 2
    return res if formato == False else moeda(res)  
    # Agora também pode retornar a metade formatada como moeda

def moeda(preço = 0, moeda = 'R$', formato=False):
    return f'{moeda}{preço:>.2f}'.replace('.', ',')  
    # A função continua formatando o valor como moeda (ex: R$10,00)
    # O parâmetro 'formato' foi adicionado, mas não está sendo usado aqui


def resumo(preço=0, taxa=10, taxar=5):  # Função que exibe um resumo do preço com aumento e redução
    print('-' * 30)  # Linha de separação visual
    print('RESUMO DO VALOR'.center(30))  # Título centralizado
    print('-' * 30)  # Linha de separação visual

    print(f'Preço analisado: \t{moeda(preço)}')  # Exibe o preço formatado como moeda
    print(f'Dobro do preço: \t{dobro(preço, True)}')  # Exibe o dobro do preço
    print(f'Metade do preço: \t{metade(preço, True)}')  # Exibe a metade do preço
    print(f'Com {taxa}% de aumento: \t{aumentar(preço, taxa, True)}')  # Exibe o preço com aumento percentual
    print(f'Com {taxar}% de redução: \t{diminuir(preço, taxar, True)}')  # Exibe o preço com redução percentual
    print('-' * 30)  # Linha de separação visual
