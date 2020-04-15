"""Exercício Python 025:
Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome."""

nome = str(input('Digite o seu nome:_ ')).strip().upper()
print('Seu nome tem Silva?:_ {}'.format('SILVA' in nome))

# poderiamos ter escrito da seguinte forma
print('Seu nome tem Silva?:_ {}'.format('SILVA' in nome.upper()))
