for i in range(1, 4):
    n = int(input(f'Digite o {i}º número: '))
    if i == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        elif n < menor:
            menor = n

print(f'O menor número foi {menor} e o maior foi {maior}!')