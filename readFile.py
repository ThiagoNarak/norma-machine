file_list = []


def readLines():
    f = open('arquivo.txt', 'r')
    for line in f:
        file_list.append(line)

# trim para tirar espaços da linha
# remover linhas vazias e identificar linhas com comentario #
# parser para identificar linha e direcionar ela para o comando correto
# criar vetor de linhas para utilizar regex
