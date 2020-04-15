'''Enunciado:
Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade 
de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia
e R$0,15 por Km rodado.'''

km = float(input('Informe a quantidade de kilometragem percorrida: '))
d = int(input('Informe a quantidade de dias utilizado: '))
Vkm = 0.15
Vd = 60
Vpg = (km * Vkm) + (d * Vd)
print('Foi percorrido {}Km em {} dias, o valor a ser pago pelo aluguel do carro é de: R${:.2f}'.format(km, d, Vpg))
