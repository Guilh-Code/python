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
