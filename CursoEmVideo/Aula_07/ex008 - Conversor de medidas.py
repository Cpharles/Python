#Escreva um algoritimo que leia um valor em metros e o exiba convertido em centímetros e milimetros
#
n = float(input('Entre com o comprimento a ser convertido:_ '))
cm = n * 100
mm = cm * 10
print('Valor em centimetros = {}cm'.format(cm))
print('Valor em milimetro = {}mm'.format(mm))
