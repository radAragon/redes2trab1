#!/usr/bin/env python
import os
import argparse
import parity_lib as pl

BLOCK_SIZE = 8


parser = argparse.ArgumentParser(description='Redes II: produz paridade de arquivo.')
parser.add_argument('filepath', type=str, help='um arquivo existente')
args = parser.parse_args()


if not os.path.exists(args.filepath):
    print('Arquivo não encontrado')
    exit(1)

with open(args.filepath, 'rb') as arq_origem:
    with open(args.filepath + '.parity', 'wb') as arq_dest:
        while True:
            buff = arq_origem.read(BLOCK_SIZE)
            if not buff:
                break  # eof

            matriz = pl.parse_bin_matrix(buff, BLOCK_SIZE)
            par_linhas = pl.get_lin_parity(matriz, BLOCK_SIZE)
            par_colunas = pl.get_col_parity(matriz, BLOCK_SIZE)

            # Mostra matriz e paridades
            for x in range(BLOCK_SIZE):
                print(matriz[x], par_linhas[x])
            for y in range(BLOCK_SIZE):
                print(' ' + str(par_colunas[y]), end=' ')
            print('\n')

            # Escreve o buffer no novo arquivo precedido dos bits de paridade
            bit_par_colunas = ''.join([str(x) for x in par_colunas])
            bit_par_linhas = ''.join([str(x) for x in par_linhas])
            bytes_paridade = bytes([int(bit_par_colunas, base=2),
                                    int(bit_par_linhas, base=2)])
            arq_dest.write(bytes_paridade)
            arq_dest.write(buff)
