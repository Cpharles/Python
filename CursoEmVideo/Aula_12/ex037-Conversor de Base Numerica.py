"""Exercício Python 037:
Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de
conversão: 1 para binário, 2 para octal e 3 para hexadecimal."""

n = int(input('Digite um número inteiro: '))
print('Escolha uma das bases para conversão:')
print('[ 1 ] converte para BINÁRIO')
print('[ 2 ] converte para OCTAL')
print('[ 3 ] converte para HEXADECIMAL')
op = int(input('Sua opção: '))
if op == 1:
    print('{} convertido para BINÁRIO é igual a {}'.format(n, bin(n)[2:]))
elif op == 2:
    print('{} convertido para OCTAL é igual a {}'.format(n, oct(n)[2:]))
elif op == 3:
    print('{} convertido para HEXADECIMAL é igual a {}'.format(n, hex(n)[2:]))
else:
    print('Opção inválida. Tente novamente.')

"""Obs.:
após a função bin/oct/hex() foi adicionado [2:]. Indica um fatiamento de string, já que teriamos como resultado no 
inicio da resposta a indicação do tipo de função, ou seja:
    para a função bin()  ->   0b...
    para a função oct()  ->   0o...
    para a função hex()  ->   0x..."""