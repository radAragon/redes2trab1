##Trabalho 1 para Redes II - UFF 2015-2

Conjunto de programas parar gerar arquivo de paridade de um arquivo existente e então avaliar e reconstruir o arquivo original ou descartar a cópia.

###Requerimentos:

* Python 3.4

###Uso:

`> python make_parity.py [test.txt]`
* Cria o arquivo [test.txt.parity] que inclui tabelas de paridade (2 bytes) a cada bloco de 8 bytes com dados originais.

`> python check_parity.py [test.txt]`
* Verifica as tabelas de paridade e reconstrói o arquivo original acrescentando [.2] ao final. Se houver erro simples em um ou mais blocos, o programa é capaz de corrigi-lo(s).
