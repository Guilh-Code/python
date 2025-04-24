# Refaça o DESAFIO 9, mostrando a TABUADA de um número que o usuário escolher, só que agora utilizando um LAÇO FOR.


num = int(input('Qual tabuada você dejesa? '))

for t in range(1,11):
    resultado = num * t
    print(f'{num} x {t} = {resultado}')
    