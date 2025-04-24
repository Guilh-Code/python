# Faça um programa que mostre na tela uma CONTAGEM REGRESSIVA para o estouro de fogos de artifício, indo de 10 até 0, com uma pausa de 1 SEGUNDO entre eles.


from time import sleep  # Importa a função sleep do módulo time, que permite pausar a execução do programa por um tempo

for r in range(10, -1, -1):  # Cria um loop que começa em 10 e vai até 0 (inclusive), contando de 1 em 1 para trás
    print(r)  # Imprime o valor atual de r na tela
    sleep(1)  # Pausa o programa por 1 segundo antes de continuar com o próximo número

print('BUM! BUM! POOOW!')  # Após a contagem regressiva, imprime a mensagem de "BUM! BUM! POOOW!"
