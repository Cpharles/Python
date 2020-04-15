#Exercício Python 017: Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente
#de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.

from math import sqrt
C_oposto = float(input('Digite o valor do cateto oposto: '))
C_adj = float(input('Digite a valor do cateto adjacente: '))
hip = sqrt(C_oposto ** 2 + C_adj ** 2)
print('O comprimento da hipotenusa {:0.2f}'.format(hip))

#sem a utillizar a lib
hip = (C_oposto ** 2 + C_adj ** 2) ** (1/2)
print('O comprimento da hipotenusa {:0.2f}'.format(hip))
