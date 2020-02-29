#Escreva um algoritimo que leia o preço de um produto e mostre seu novo preço com 5% de desconto.
valor = float(input('Qual o valor do produto?_R$'))
valDesc = valor - (valor * 0.05)
print('Valor do produto com desconto de 5% - R${:0.2f}'.format(valDesc))
