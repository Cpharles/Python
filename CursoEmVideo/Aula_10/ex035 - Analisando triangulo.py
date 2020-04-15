"""Exercício Python 035:
Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo."""

print('-=-' * 20)
print('ANALISANDOR DE TRINANGULO')
print('-=-' * 20)
A = float(input('Primeiro segmento:_'))
B = float(input('Segundo seguimento:_'))
C = float(input('Terceiro seguimento:_'))
if (B-C < A < B+C) and (A-C < B < A+C) and (A-B < C < A+B):
    print('O seguimentos acima PODEM FORMAR triângulo!')
else:
    print('Este seguimento NÂO PODEM FORMAR triângulo!')

