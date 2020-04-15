#Escreva um algoritimo que leia um numero inteiro e mostre na tela o seu sucessor e seu antecessor.
#
n = int(input('Entre com um número:_ '))
sus = n + 1
ant = n - 1
print('O antecessor do numero {} é {}'.format(n, ant), end=' ')
print('e o sucessor do número {} é {}'.format(n, sus))