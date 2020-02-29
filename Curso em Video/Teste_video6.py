#n1 = input('Digite um valor: ')
#n2 = input('Digite outro valor: ')
#na situação superior temos a concatenação das declarações
n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
#na situação atual em uso temos a somatoria de numeros inteiros, usando a função int()
s = n1 + n2
#print('A soma entre', n1, '+', n2, 'é igual = ', s)  esta sintax não é mais utilizado, mas ainda funciona
print('A soma entre {} e {} é igual = {}'.format(n1, n2, s))#outra forma de apresentar
