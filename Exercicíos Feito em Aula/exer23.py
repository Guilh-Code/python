teste = []

teste.append('Guilherme')
teste.append(19)

galera = []

galera.append(teste[:])
teste[0] = 'Emily'
teste[1] = 22
galera.append(teste[:])

print(galera)