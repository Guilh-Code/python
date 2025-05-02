# Crie um programa que tenha uma TUPLA totalmente preenchida com uma contagem por extenso, de ZERO até VINTE. Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.


numeros_escrita = (
    "Zero", "Um", "Dois", "Três", "Quatro", "Cinco", "Seis", "Sete", "Oito", "Nove", "Dez", "Onze", "Doze", "Treze", "Quatorze", "Quinze", "Dezesseis", "Dezessete", "Dezoito", "Dezenove", "Vinte"
    )


while True:
    num = int(input("Digite um número de 0 a 20: "))
    if 0 <= num <= 20:
        break
    print("Tente novamente. Número fora do intervalo")


print(f"Você digitou o número {numeros_escrita[num]}")

