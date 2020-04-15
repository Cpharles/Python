'''Enunciado:
Escreva um algoritimo que leia a largura e a altura de uma parede em metros, 
calcule a sua área e a quantidade de tinta necessária para pintá-la,
sabendo que cada litro de tinta, pinta uma área de 2m2. '''

print('Calculo da quantidade tinta para pintar uma parede:')
print('obs.:fornecer o valor em metros')
H = float(input('Forneça a altura da parede: '))
L = float(input('Forneça a largura da parede: '))
s = H * L
print('Sua parede tem uma dimensão de {}x{} e sua área é de {}m2'.format(H, L, s))
Qntinta = s / 2
print('Será necessário {:0.1f}lts para pintar {}m2'.format(Qntinta, s))
