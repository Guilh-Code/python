# Refaça o DESAFIO 9, mostrando a TABUADA de um número que o usuário escolher, só que agora utilizando um LAÇO FOR.


num = int(input('Qual tabuada você deseja? '))  # Pede ao usuário um número e converte a resposta para inteiro

for t in range(1, 11):  # Cria um loop de 1 até 10 (inclusive) — os valores da tabuada
    print(f'{num} x {t:2} = {num * t}')  # Exibe a multiplicação formatada: ex. 5 x 1 = 5, 5 x 2 = 10, etc.
