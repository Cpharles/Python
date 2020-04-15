#Exercício Python 018: Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno,
# cosseno e tangente desse ângulo.

from math import sin, cos, tan, radians
ang = float(input('Digite um angulo: '))
s = sin(radians(ang)) #seno
c = cos(radians(ang)) #cosseno
t = tan(radians(ang)) #tangente
print('O angulo de {} tem o SENO de {:.2f}'.format(ang, s))
print('O angulo de {} tem o COSSENO de {:.2f}'.format(ang, c))
print('O angulo de {} tem a TANGENTE de {:.2f}'.format(ang, t))
