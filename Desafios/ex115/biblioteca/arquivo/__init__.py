# B) Vamos ver como fazer acesso a arquivos usando o Python.

from interface import *  # Importa todas as funções do módulo interface (por exemplo, a função cabeçalho)

# Verifica se o arquivo existe
def arquivoExiste(nome):
    try:
        with open(nome, 'rt'):  # Tenta abrir o arquivo no modo de leitura de texto
            pass  # Se conseguir abrir, o arquivo existe
    except FileNotFoundError:  # Se o arquivo não for encontrado
        return False  # Retorna False indicando que o arquivo não existe
    else:
        return True  # Retorna True se o arquivo foi aberto com sucesso


# Cria um arquivo novo
def criarArquivo(nome):
    try:
        with open(nome, 'wt+'):  # Cria um novo arquivo (ou sobrescreve se já existir), modo escrita e leitura
            pass  # Não faz nada além de criar e fechar o arquivo
    except OSError:  # Se ocorrer erro ao tentar criar o arquivo
        print('Houve um ERRO na criação do arquivo!')  # Exibe mensagem de erro
    else:
        print(f'Arquivo {nome} criado com sucesso!')  # Confirma que o arquivo foi criado


# Lê e exibe o conteúdo do arquivo
def lerArquivo(nome):
    try:
        with open(nome, 'rt') as a:  # Abre o arquivo em modo leitura
            cabeçalho('PESSOAS CADASTRADAS')  # Chama a função cabeçalho (importada da interface)
            for linha in a:  # Percorre cada linha do arquivo
                dado = linha.strip().split(';')  # Remove \n e divide a linha pelo separador ';'
                print(f'{dado[0]:<30}{dado[1]:>3} anos')  # Exibe nome alinhado à esquerda e idade à direita
    except:  # Se ocorrer qualquer erro ao abrir ou ler
        print('ERRO ao ler o arquivo!')  # Mensagem de erro genérica


# Cadastra uma nova pessoa no arquivo
def cadastrar(arq, nome='desconhecido', idade=0):
    try:
        with open(arq, 'at') as a:  # Abre o arquivo no modo append (acrescentar texto no final)
            try:
                a.write(f'{nome};{idade}\n')  # Escreve os dados no formato "nome;idade"
            except:  # Se falhar ao tentar escrever
                print('Houve um ERRO na hora de escrever os dados!')  # Mensagem de erro
            else:
                print(f'Novo registro de {nome} adicionado.')  # Confirma que os dados foram gravados
    except:  # Se não conseguir abrir o arquivo
        print('Houve um ERRO na abertura do arquivo!')  # Mensagem de erro
