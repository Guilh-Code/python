''' Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues. OBS:

considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1. '''


pprint('=' * 30) 
print('{:^30}'.format('BANCO DEV'))  # Imprime "BANCO DEV" centralizado em 30 espaços
print('=' * 30)

valor = int(input('Que valor você quer sacar? R$'))  # Pede o valor que o usuário quer sacar

total = valor  # Guarda o valor total para controle
ced = 50  # Começa pelas cédulas de R$50
totced = 0  # Contador de cédulas da nota atual

while True:  # Loop infinito até quebrar com break
    
    if total >= ced:  # Se ainda dá para sacar usando a cédula atual
        total -= ced  # Diminui o valor da cédula do total
        totced += 1  # Conta uma cédula usada
    
    else:
        
        if totced > 0:  # Se foram usadas cédulas deste valor
            print(f'Total de {totced} cédulas de R${ced}')  # Mostra quantas cédulas foram usadas
        
        if ced == 50:  # Troca para a próxima cédula menor
            ced = 20
        
        elif ced == 20:
            ced = 10
        
        elif ced == 10:
            ced = 1
        totced = 0  # Reseta o contador de cédulas
        
        
        if total == 0:  # Se acabou o valor, para o loop
            break

print('=' * 30)  # Imprime linha final
print('Volte sempre ao BANCO DEV! Tenha um bom dia!')  # Mensagem de despedida
