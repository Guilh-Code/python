# Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições..


# Define a função 'voto' que recebe o ano de nascimento como parâmetro
def voto(ano):
    # Importa a função 'date' de dentro do módulo 'datetime'
    from datetime import date

    
    # Pega o ano atual
    atual = date.today().year
    # Calcula a idade com base no ano de nascimento
    idade = atual - ano

   
    # Verifica se a idade é menor que 16 anos
    if idade < 16:
        return f'Com {idade} anos: NÃO VOTA.'
    
    # Verifica se a idade está entre 16 e 17 ou acima de 65 (voto opcional)
    elif 16 <= idade < 18 or idade > 65:
        return f'Com {idade} anos: VOTO OPCIONAL.'

    # Caso contrário, o voto é obrigatório (entre 18 e 65 anos)
    else: 
        return f'Com {idade} anos: VOTO OBRIGATÓRIO.'


# ====== Programa principal ======
# Solicita ao usuário o ano de nascimento e converte para inteiro
nasc = int(input('Em que ano você nasceu? '))
# Chama a função 'voto' com o ano informado e imprime o resultado
print(voto(nasc))

