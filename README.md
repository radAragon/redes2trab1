##Trabalho 1 para Redes II - UFF 2015-2

Conjunto de programas gerar um arquivo de paridade de um arquivo existente e então avaliar e reconstruir o arquivo original ou descartar a cópia.

###Requerimentos:

* Python 3.4

###Uso:

`> python make_parity.py [test.txt]`
* Cria o arquivo [test.txt.parity] que inclui as tabelas de paridade em blocos de 8 bytes.

`> python check_parity.py [test.txt]`
* Verifica as tabelas de paridade e reconstrói o arquivo original acrescentando [.2] ao final. Se houver um erro simples em um ou mais blocos, o programa é capaz de corrigi-lo.
