#Escreva um algoritimo que leia quanto dinheiro uma pessoa tem na carteira e mostre 
# quantos dólares ela pode comprar. Considere US$1,00 = R$3,27

real = float(input('Quanto dinheiro você tem disponível:_ '))
ValDollar = 3.27
Conv = real / ValDollar
print('O valor do dollar vale: US$1,00 = R$3,27 \n Você poderá comprar: US${:0.2f}'.format(Conv))
