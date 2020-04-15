"""Exercício Python 031:
Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km
para viagens de até 200Km e R$0,45 parta viagens mais longas."""

dist = float(input('Qual é a distancia da sua viagem?_'))
print('Você esta preste a começar uma viagem de {:.1f}km.'.format(dist))
if dist <= 200:
    preço = dist * 0.5
else:
    preço = dist * 0.45
print('O preço da sua passagem será de R${:.2f}'.format(preço))
