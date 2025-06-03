

def teste_velocidade(velo):
    if velo < 80:
        print('Tenha um bom dia! Dirija com segurança.')
    else:
        multa = (velo - 80) * 7
        print('MULTADO! Você excedeu o limite de velocidade de 80Km/h')
        print(f'Você deve pagar uma multa de R${multa:.2f}')


velocidade = int(input('Qual a velocidade atual do carro? '))
teste_velocidade(velocidade)
