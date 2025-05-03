# Crie um programa que tenha uma TUPLA totalmente preenchida com uma contagem por extenso, de ZERO até VINTE. Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.


# Tupla contendo os números de 0 a 20 escritos por extenso
numeros_escrita = (
    "Zero", "Um", "Dois", "Três", "Quatro", "Cinco", "Seis", "Sete", "Oito", "Nove",
    "Dez", "Onze", "Doze", "Treze", "Catorze", "Quinze", "Dezesseis", "Dezessete", "Dezoito", "Dezenove", "Vinte"
)


# Loop infinito para garantir que o usuário digite um número válido
while True:
    
    # Solicita um número ao usuário
    num = int(input("Digite um número de 0 a 20: "))

    # Verifica se o número está entre 0 e 20 (inclusive)
    if 0 <= num <= 20:
        break  # Se o número for válido, sai do loop

    # Caso o número esteja fora do intervalo, exibe mensagem de erro
    print("Tente novamente. ", end=" ")


# Exibe o número por extenso, acessando a posição correspondente na tupla
print(f"Você digitou o número {numeros_escrita[num]}")
