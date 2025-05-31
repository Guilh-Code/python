# Use while. O programa deve pedir uma senha até o usuário digitar a senha correta (python123).


while True:
    s = input('Qual é a senha: ')
    if s != 'python123':
        print('Senha Incorreta.')
    else:
        print('Acesso liberado!')
        break