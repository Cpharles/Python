n1 = int(input('Um valor: '))
n2 = int(input('Outro valor '))
print('A soma vale {:=^5}'.format(n1 + n2))
s = n1 + n2   #soma
m = n1 * n2   #mutiplicação
d = n1 / n2   #divisão
di = n1 // n2 #divisão inteira
e = n1 ** n2  #exponenciação
print('A soma é {}, O produto é {}, e a divisão é {}'.format(s, m, d))
#acrecentando  | end=' ' | no final da função print, o proximo print continua na mesma linha do anterior
print('Divisão inteira é {}, e potência é {}'.format(di, e), end=' ')
#3 casa depois da virgula
print('Divisão com numero de casa é {:.3f}'.format(d))
#para quebrar a linha do print se usa \n
print('A soma é {},\n O produto é {},\n e a divisão é {:.2f}'.format(s, m, d))
