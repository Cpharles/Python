nome = input('Qual o seu nome? ')
print('Prazer em te conhecer {:20}!'.format(nome)) #limita em 20 espaço p/ preenchimento
print('Prazer em te conhecer {:<20}!'.format(nome)) #alinhado a esquerda
print('Prazer em te conhecer {:>20}!'.format(nome)) #alinhado a direita
print('Prazer em te conhecer {:^20}!'.format(nome)) #centralizado
print('Prazer em te conhecer {:=^20}!'.format(nome))#acrecenta sinal de igual 