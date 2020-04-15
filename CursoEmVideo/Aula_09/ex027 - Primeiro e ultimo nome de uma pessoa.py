"""Exercício Python 027:
Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente."""

nome = str(input('Digite seu nome completo:_')).strip()
lista = nome.split()
indice = len(lista)
print('Seu primeiro nome é:_{}'.format(lista[0]))
print('Seu ultimo nome é:_{}'.format(lista[indice-1]))
