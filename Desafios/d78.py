# Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.


valores = []  # Lista para guardar os valores digitados

# Laço para receber 5 valores
for i in range(5):
    num = int(input(f"Digite um valor para a posição {i}: "))
    valores.append(num)  # Adiciona o número à lista


# Determina o maior e o menor valor da lista
maior = max(valores)
menor = min(valores)

# Mostra a lista completa
print(f"\nVocê digitou os valores: {valores}")


# Mostra o maior valor e suas posições
print(f"O maior valor foi {maior} nas posições: ", end="")

for i, v in enumerate(valores):  # Percorre a lista com índice e valor
    if v == maior:
        print(f"{i}.. ", end="")  # Mostra a posição do maior valor


# Mostra o menor valor e suas posições
print(f"\nO menor valor foi {menor} nas posições: ", end="")

for i, v in enumerate(valores):
    if v == menor:
        print(f"{i}.. ", end="")  # Mostra a posição do menor valor
