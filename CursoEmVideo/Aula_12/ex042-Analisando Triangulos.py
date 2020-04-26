"""Exercício Python 042:
Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
- EQUILÁTERO: todos os lados iguais
- ISÓSCELES: dois lados iguais, um diferente
- ESCALENO: todos os lados diferentes"""

print('-=-' * 20)
print('ANALISADOR DE TRIANGULO')
print('-=-' * 20)
A = float(input('Primeiro seguimento:_'))
B = float(input('Segundo seguimento:_'))
C = float(input('Terceiro seguimento:_'))
if (B-C < A < B+C) and (A-C < B < A+C) and (A-B < C < A+B):
    print('Os seguimento podem formar um triângulo ', end='')
    if A == B and A == C:
        print('"EQUILÁTERO"')
    elif A == B or A == C or B == C:
        print('"ISÓSCELES"')
    elif A != B and A != C and B != C:
        print('"ESCALENO"')
else:
    print('Estes seguimentos não podem formar um triângulo!')
