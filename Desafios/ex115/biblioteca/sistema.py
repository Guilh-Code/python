# C) Vamos finalizar o projeto de acesso a arquivos em Python.

from interface import *  # Importa funções da interface, como cabeçalho() e menu()
from arquivo import *    # Importa funções de manipulação de arquivos (lerArquivo, criarArquivo, etc.)
from time import sleep   # Importa sleep para pausar o programa entre ações


arq = 'cursoemvideo.txt'  # Nome do arquivo que será utilizado

# Verifica se o arquivo já existe
if not arquivoExiste(arq):
    print('Arquivo não encontrado. Criando arquivo...')
    criarArquivo(arq)  # Cria o arquivo se ele não existir
else:
    print('Arquivo já existe.')


# Loop principal do menu
while True:
    # Mostra o menu e armazena a escolha do usuário
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar nova Pessoa', 'Sair do Sistema'])

    if resposta == 1:
        # Opção 1: Exibe os dados cadastrados
        lerArquivo(arq)

    elif resposta == 2:
        # Opção 2: Cadastra nova pessoa
        cabeçalho('NOVO CADASTRO')
        nome = str(input('Nome: '))  # Solicita o nome do usuário
        idade = leiaInt('Idade: ')   # Solicita a idade (função leiaInt deve validar)
        cadastrar(arq, nome, idade)  # Grava os dados no arquivo

    elif resposta == 3:
        # Opção 3: Sai do sistema
        cabeçalho('Saindo do sistema... Até logo!')
        break  # Encerra o loop

    else:
        # Caso o usuário escolha uma opção inválida
        print('\033[31mERRO! Digite uma opção válida!\033[m')

    sleep(1.5)  # Aguarda 1.5 segundos antes de repetir o menu
