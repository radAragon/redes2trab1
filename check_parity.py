#!/usr/bin/env python
import os
import argparse
import parity_lib as pl

BLOCK_SIZE = 8


parser = argparse.ArgumentParser(description='Redes II: valida arquivo de paridade.')
parser.add_argument('filepath', type=str, help='um arquivo existente')
args = parser.parse_args()

if not args.filepath.endswith('.parity'):
    args.filepath += '.parity'

if not os.path.exists(args.filepath):
    print('Arquivo de paridade não encontrado')
    print('Necessário executar make_parity primeiro')
    exit(1)

with open(args.filepath, 'rb') as arq_origem:
    namedest = args.filepath.partition('.parity')[0] + '.2'
    with open(namedest, 'wb') as arq_dest:
        while True:
            buff = arq_origem.read(BLOCK_SIZE + 2)
            if not buff:
                break  # eof

            if len(buff) < 3:
                print('Erro: bloco menor que 3 bytes detectado')
                break

            dados = bytes([buff[x] for x in range(2, len(buff))])
            dados_matriz = pl.parse_bin_matrix(dados, BLOCK_SIZE)
            par_linhas = pl.get_lin_parity(dados_matriz, BLOCK_SIZE)
            par_colunas = pl.get_col_parity(dados_matriz, BLOCK_SIZE)

            buff_par_colunas = []
            for b in pl.bits([buff[0]], BLOCK_SIZE):
                buff_par_colunas.append(b)

            buff_par_linhas = []
            for b in pl.bits([buff[1]], BLOCK_SIZE):
                buff_par_linhas.append(b)

            col_err = []
            lin_err = []

            # Mostra matriz e paridades reais, paridades lidas no arquivo e erros
            for x in range(BLOCK_SIZE):
                err = None
                if buff_par_linhas[x] != par_linhas[x]:
                    err = x
                    lin_err.append(x)
                sig = '' if not err else '<'
                print(dados_matriz[x], par_linhas[x], buff_par_linhas[x], sig)

            for y in range(BLOCK_SIZE):
                print(' ' + str(par_colunas[y]), end=' ')
            print('')

            for y in range(BLOCK_SIZE):
                print(' ' + str(buff_par_colunas[y]), end=' ')
            print('')

            for y in range(BLOCK_SIZE):
                err = None
                if buff_par_colunas[y] != par_colunas[y]:
                    err = y
                    col_err.append(y)
                sig = '   ' if not err else ' ^ '
                print(sig, end='')
            print('\n')

            if (len(col_err) + len(lin_err)) > 2:
                print('Erro: bloco com erros demais, impossível corrigir')
            elif (len(col_err) + len(lin_err)) == 1:
                print('Erro: bloco com erro parcial, impossível corrigir')
            elif (len(col_err) + len(lin_err)) == 2:
                print('Corrigindo bit', lin_err[0], col_err[0])
                if dados_matriz[lin_err][col_err] == 1:
                    dados_matriz[lin_err][col_err] = 0
                else:
                    dados_matriz[lin_err][col_err] = 1

            for x in range(len(dados)):
                bits = ''.join([str(y) for y in dados_matriz[x]])
                new_buff = bytes([int(bits, base=2)])
                arq_dest.write(new_buff)
