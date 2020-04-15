#tratando as variaveis com atributos
a = input('Digite algo: ')
print('O tipo primitivo desse valor é ', type(a))
print('Só tem espaços? ', a.isspace())
print('Só tem numero?', a.isnumeric())
print('É alfabético? ', a.isalpha())
print('É alfanumerico? ', a.isalnum())
print('Esta em maiúsculas? ', a.isupper())
print('Esta em minúsculas? ', a.islower())
