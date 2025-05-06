# Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.  Ex: escreva(‘Olá, Mundo!’) 
# Saída: ~~~~~~~~~ 
#       Olá, Mundo!
#        ~~~~~~~~~


# Define uma função chamada 'escreva' que recebe uma mensagem (msg) como parâmetro
def escreva(msg):
    # Calcula o tamanho da moldura com base no comprimento da mensagem + 4 caracteres
    tam = len(msg) + 4
    
    # Imprime uma linha de til (~) para o topo da moldura
    print('~' * tam)
    # Imprime a mensagem centralizada com dois espaços de margem em cada lado
    print(f'  {msg}')
    # Imprime outra linha de til (~) para a base da moldura
    print('~' * tam)


# Chama a função 'escreva' com a mensagem "Guilherme Rodrigues"
escreva('Guilherme Rodrigues')

# Chama a função 'escreva' com a mensagem "Curso de Python"
escreva('Curso de Python')

# Chama a função 'escreva' com a mensagem "Olá, Mundo!"
escreva('Olá, Mundo!')
