"""Exercício Python 022: Crie um programa que leia o nome completo de uma pessoa e mostre:
- O nome com todas as letras maiúsculas e minúsculas.
- Quantas letras ao todo (sem considerar espaços).
- Quantas letras tem o primeiro nome."""
nome = str(input('Digite o nome completo: ')).strip()
#colocando a função strip() no final desta variável, será ignora espaços vazios no inicio e termino da string
print('Analisando seu nome...')
print('Nome em maiúsculo:_ {}'.format(nome.upper()))
print('Nome em minúsculo:_ {}'.format(nome.lower()))
comprimento = len(nome) - nome.count(' ')
print('Comprimento do nome:_ {}'.format(comprimento))
print('Comprimento do primeiro nome:_ {}'.format(nome.find(' ')))

# podemos fazer também da seguinte forma a contagem do primeiro nome:
dividir = nome.split()
#print(dividir)
print('Seu primeiro nome:_ {} e o comprimento do primeiro nome:_ {}'.format(dividir[0], len(dividir[0])))
