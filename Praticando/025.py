arquivo = open('arqText.txt', 'w')

arquivo.write('Curso Python \n')
arquivo.write('Aula Pratica')
arquivo.close()

# Leitura do Arquivo de Texto  

leitura = open('arqText.txt', 'r')
print(leitura.read())
leitura.close()