# Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações:
'''Quantidade de notas     
A maior nota
A menor nota
A média da turma
A situação (opcional).'''


# Função 'notas' que recebe várias notas (usando *n) e um parâmetro opcional 'sit'
def notas(*n, sit=False):
    r = dict()  # Cria um dicionário para armazenar os resultados

    r['total'] = len(n)         # Quantidade de notas informadas
    r['maior'] = max(n)         # Maior nota
    r['menor'] = min(n)         # Menor nota
    r['média'] = sum(n)/len(n)  # Média das notas


    # Se 'sit' for True, adiciona a situação com base na média
    if sit:
        if r['média'] > 7:
            r['situação'] = 'BOA'
        elif r['média'] >= 5:
            r['situação'] = 'RAZOÁVEL'
        else:
            r['situação'] = 'RUIM'

    return r  # Retorna o dicionário com os dados


# ====== Programa principal ======

# Chamada da função passando várias notas e solicitando a situação
resp = notas(5.5, 2.5, 9, 8.5, sit=True)
# Exibe o resultado retornado
print(resp)

