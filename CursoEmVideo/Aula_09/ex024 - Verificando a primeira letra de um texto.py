"""Exercício Python 024:
Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome "SANTO"."""

cid = str(input('Digite o nome da cidade:_ ')).strip()
nome = cid.upper().split() #vai para maiúscula e separa em listas
print(nome)
print(nome[0] == 'SANTO')


#poderiamos fazer também:
print(cid[:5].upper() == 'SANTO') #pego as 5 primeiras letras converto para maiúsculo e comparo
