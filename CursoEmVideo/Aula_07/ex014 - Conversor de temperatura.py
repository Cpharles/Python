#Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.

c = float(input('Informe a temperatura em °C: '))
f = ((9 * c) / 5) + 32
#regra de precedencia para calculo, onde ñ será necessário usar os parenteses
f = 9 * c / 5 + 32 #respeita a orde de operação
print('A temperatura de {}°C corresponte a {}°F'.format(c, f))
