# Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.


# Solicita ao usuário que digite uma expressão e armazena como string
expr = str(input('Digite a expressão: '))

# Cria uma lista (pilha) para controlar os parênteses
pilha = []

# Percorre cada caractere da expressão
for símb in expr:
    
    # Se o caractere for um parêntese de abertura
    if símb == '(':
        # Adiciona à pilha
        pilha.append('(')
    
    # Se o caractere for um parêntese de fechamento
    elif símb == ')':
        
        # Verifica se há um parêntese de abertura na pilha para fechar
        if len(pilha) > 0:
            # Remove o último parêntese de abertura (fechando o par)
            pilha.pop()
        else:
            # Se não há parêntese de abertura, há um erro – adiciona o de fechamento e para o loop
            pilha.append(')')
            break


# Após o loop, se a pilha estiver vazia, todos os parênteses foram fechados corretamente
if len(pilha) == 0:
    print('Sua expressão está VÁLIDA!')
else:
    # Se a pilha não estiver vazia, há parênteses abertos ou fechados sem correspondência
    print('Sua expressão está ERRADA!')
