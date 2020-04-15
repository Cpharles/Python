"""Exercício Python 028:
Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar
descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu."""

from random import randint
n = randint(0, 5)
print('-=-' * 20)
print(n)
print('Vou pensar em um número entre 0 à 5. Tente advinhar...')
print('-=-' * 20)
numero = int(input('Digite seu palpite:_ ')) # jogador joga
if numero == n:
    print('PARABENS!!!  VOCÊ ACERTOU O NÚMERO ESCOLHIDO PELO PC!')
else:
    print('Você errou, o número que o PC escolheu foi: {}'.format(n))
    print('TENTE NOVAMENTE!')

