"""Exercício Python 038:
Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem:
- O primeiro valor é maior
- O segundo valor é maior
- Não existe valor maior, os dois são iguais"""

num1 = int(input('Primeiro número:_'))
num2 = int(input('Segundo número:_'))
if num1 > num2:
    print('O PRIMEIRO valor é maior')
elif num2 > num1:
    print('O SEGUNDO valor é maior')
elif num1 == num2:
    print('Não existe valor maior, os dois são iguais')