import random, time

c = 0

print('VOU PENSAR EM NÚMERO DE 1 A 10. TENTE ADIVINHAR...')
('-=' * 20)

num_maquina = random.randint(1, 100)


while True:
    tent = int(input('Em que número eu pensei? '))
    print('PROCESSANDO...')
    time.sleep(0.5)
    c += 1

    if tent == num_maquina:
        print('Você ACERTOU!!!')
        break
    elif tent > num_maquina:
        print('Menos...')
    elif tent < num_maquina:
        print('Mais...')

    


print(f'Você deu {c} tentativas até acertar.')