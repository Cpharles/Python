"""Exercício Python 030:
Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR."""

n = int(input('Digite um número inteiro qualquer:_'))
resto = n % 2
if resto == 1:
    print('O número {} é "IMPAR"'.format(n))
else:
    print('O número {} é "PAR"'.format(n))
