
def cidade_que_nasceu(cid):
    if cid[:3].upper() == 'SÃO':
        print(f'Verdadeiro, você mora em {cid}!')
    else:
        print('Falso, você mentiu para mim...')

def Procurador_Sobrenome(n):
    if 'RODRIGUES' in n:
        print('Verdadeiro')
    else:
        print('Falso')

def primeiro_e_ultimo_nome(n):
    print('Muito prazer em te conhecer!')
    lista = n.split()

    print(f'Seu primeiro nome é {lista[0]}')
    print(f'Seu último nome é {lista[-1]}')


nasc = str(input('Em que cidade você nasceu? ')).upper()
cidade_que_nasceu(nasc)

nome = str(input('Digite o seu nome completo: ')).upper().strip()
Procurador_Sobrenome(nome)
primeiro_e_ultimo_nome(nome)
