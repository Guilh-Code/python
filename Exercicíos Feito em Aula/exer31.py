
def contador(*num):
    tam = len(num)
    print(f'Recebi os valores {num} e são ao todo {tam} números')
    print('-' * 20)

def soma(*valores):
    s = 0
    for num in valores:
        s += num
    print(f'Somando os valores {valores} temos {s}')




contador(2, 1, 7)

contador(8, 0)

contador(4, 4, 7, 6, 2)


print('-' * 40)


soma(5, 2)

soma(2, 9, 4)
