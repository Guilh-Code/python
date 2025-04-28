# Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo.


while True:  # Inicia um loop infinito (vai rodar até o usuário pedir para parar)
    
    n = int(input('Quer ver a tabuada de qual valor? '))  # Pede para o usuário escolher um número
    print('-' * 35)  
    
    if n < 0:  # Se o número digitado for negativo
        break  # Interrompe o loop (encerra o programa)
   
    for cont in range(1, 11):  # Cria um loop de 1 até 10 (inclusive) para montar a tabuada
        print(f'{n} x {cont} = {n * cont}')  # Mostra a multiplicação atual da tabuada

    print('-' * 35)  
    
# Quando o usuário digitar um número negativo, sai do loop e imprime a mensagem final
print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')
