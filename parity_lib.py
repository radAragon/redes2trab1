def bits(buff, block_size):
    # Separa bits do buffer
    for b in buff:
        for i in reversed(range(block_size)):
            yield (b >> i) & 1


def parse_bin_matrix(buff, block_size):
    # Preenche a matriz com bits do buffer
    print('\nBloco:', buff)
    matriz = [[0 for x in range(block_size)] for x in range(block_size)]
    altura = 0
    largura = 0
    for b in bits(buff, block_size):
        if largura >= block_size:
            altura += 1
            largura = 0

        matriz[altura][largura] = b
        largura += 1

    return matriz


def get_lin_parity(matriz, block_size):
    # Obtém paridade das linhas
    paridade = []
    for lin in range(block_size):
        soma = 0
        for col in range(block_size):
            soma += matriz[lin][col]

        paridade.append(soma % 2)

    return paridade


def get_col_parity(matriz, block_size):
    # Obtém paridade das colunas
    paridade = []
    for col in range(block_size):
        soma = 0
        for lin in range(block_size):
            soma += matriz[lin][col]

        paridade.append(soma % 2)

    return paridade
