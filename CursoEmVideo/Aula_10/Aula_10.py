# condição simples:
nome = str(input('Qual o seu nome?:_ '))
if nome == 'Gustavo':
    print('Que nome legal!')
print('Bom dia {}!'.format(nome))

# condição composta:
nome = str(input('Qual o seu nome?:_ '))
if nome == 'Gustavo':
    print('Que nome legal!')
else:
    print('Seu nome é normal!')
print('Bom dia {}!'.format(nome))

#condição simplificada:
ni = float(input('Digite a primeira nota:_ '))
n2 = float(input('Digite a segunda nota:_ '))
m = (n1 + n2)/2
print('A sua média foi {:.1f}'.format(m))
print('Parabens!' if m >=6 else 'Estude mais!')
