

def pedagio(v):
    if v < 200:
        valor = v * 0.50
        print(f'Você esta preste de iniciar uma viagem de {v}Km/h')
        print(f'E o preço do pedagio é de R${valor:.2f}')
    
    else:
        valor = v * 0.45
        print(f'Você esta preste de iniciar uma viagem de {v}Km/h')
        print(f'E o preço do pedagio é de R${valor:.2f}')


velec = int(input('Qual a distância da viagem? '))
pedagio(velec)

