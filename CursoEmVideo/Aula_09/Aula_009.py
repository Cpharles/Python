frase = 'Curso em Vídeo Python'
# C u r s o   e m   V i d e  o    P  y  t  h  o  n
# 0 1 2 3 4   5 6   7 8 9 10 11   12 13 14 15 16 17
# lembrando que no fatiamento o ultimo numero não é contado pois a sequencia inicia em 0
# espaço tambem é contado, letra maiúscola e minúscula é diferente
print(frase)
print(frase[3:13]) #inicia na posição 2 (s) até posição 12 (o)
print(frase[:13]) #a partir do inicio até posição 12
print(frase[3:]) #da posição 2 até o ultima posição da frase
print(frase[1:15:2]) #da posição 1 até 14 pulando de 2 em 2
print(frase[1::2]) #da posição 1 até o final pulando de 2 em 2
print(frase[::2]) #do inicio até o final da streng(frase) pulando de 2 em 2
print(frase.count('o')) #conta quantas letras 'o' tem na streng(frase)
print(len(frase)) #conta o comprimento da string
print(len(frase.strip())) #conta o comprimento da string mas ñ conta os espaço antes do inicio e depois da string
print(frase.replace('Python', 'Android')) #substitui partes da string
frase = frase.replace('Python', 'Android')#usando como variável
print(frase)
print('Curso' in frase) #verifica se se algo esta dentro da string
print(frase.find('Curso')) #procura parte da string e retorna a sua posição inicial
print(frase.find('video')) #quando não é encontrado parte da string retorna (-1)
print(frase.lower().find('vídeo')) #passa para minúscula e procura por parte da string em minúsculo
print(frase.split()) #cria uma nova lista da string separando cada palavra
dividido = frase.split() #como variável
print(dividido[0]) #cria nova lista só que monstrando a primeira lista
print(dividido[2][3]) #mostra a terceira letra da lista 2

# Uma forma de imprimir um bloco de nota usamos 3x aspas duplas no inicio e no fim do bloco
print("""Teste de texto grande como um bloco de notas com várias linhas
Teste de texto grande como um bloco de notas com várias linhas
Teste de texto grande como um bloco de notas com várias linhas
Teste de texto grande como um bloco de notas com várias linhas""")

