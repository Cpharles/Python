"""Formatação de testo a ser impresso no terminal:

sintaxe:  \033[Style; Text; Background m
          \033[S; T; Bm """
#exemplo:
print('\033[1;31;43mOlá, Mundo!')
# ou
print('\033[1;31;43mOlá, Mundo!\033[m')
print('\033[4;30;45mOlá, Mundo!\033[m')

#exemplo 2
a = 3
b = 5
print('Os valores são: \033[32m{}\033[m e \033[31m{}\033[m!!!'.format(a, b))
nome = 'Guanabara'
print('Olá muito prazer em te conhecer, {}{}{}!!'.format('\033[4;34m', nome, '\033[m'))

#exemplo 3
nome = 'Charles'
cores = {'limpa':'\033[m',
         'azul':'\033[34m',
         'amarelo':'\033[33m',
         'pretobranco':'\033[7:30m'}
print('Olá muito prazer em te conhecer, {}{}{}!!'.format(cores['amarelo'], nome, cores['limpa']))

"""TABELA
STYLE   TEXT    BACK
0       30      40
1       31      41
4       32      42
7       33      43
        34      44
        35      45
        36      46
        37      47"""

