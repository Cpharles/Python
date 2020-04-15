"""Exercício Python 026:
Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra "A",
em que posição ela aparece a primeira vez e em que posição ela aparece a última vez."""

frase = str(input('Digite uma frase:_ ')).strip().lower()
import unidecode # esta lib trata string com acentuação
print('A letra "A" aparece ({}) vezes na frase.'.format(unidecode.unidecode(frase).count('a')))
print('A primeira letra "A" aparece na posição:_{}'.format(frase.find('a') + 1))
print('A última letra "A" apareceu na posição:_{}'.format(frase.rfind('a') + 1))

