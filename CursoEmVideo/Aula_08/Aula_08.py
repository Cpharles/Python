#Utilizando biblioteca do python
#para utilizarmos uma lib vamos usar a função 'import' antes do nome da lib
# o unico ponto que devemos observar que nesta sintax importamos todas as funcionabilidades da lib
import math
num = int(input('Digite um numero: '))
raiz = math.sqrt(num)
print('A raiz de {} é igual a {}'.format(num, raiz))
print('A raiz de {} é igual a {}'.format(num, math.ceil(raiz))) 
print('A raiz de {} é igual a {}'.format(num, math.floor(raiz)))
    """ ceil  - arredonda para cima
     floor - arredonda para baixo
     trunc - elimina tudo da virgula para frente
     pow   - calculo da potência
     sqrt  - raiz quadrada
     factorial -  fotoração"""


#agora para importarmos uma funcionabilidade especifica da lib, devemos usar a seguinte sintaxe
#desta forma não é necessário escrever o nome da lib antes de cada função
from math import sqrt
num = int(input('Digite um numero: '))
raiz = sqrt(num)
print('A raiz de {} é igual a {}'.format(num, raiz))
# outro exemplo:
from math import sqrt, ceil
num = int(input('Digite um numero: '))
raiz = sqrt(num)
print('A raiz de {} é igual a {}'.format(num, ceil(raiz)))

#Buscando informação das libs.
#Para ver as funcionalidades das lib, consultar a doc no site python em www.python.org
#ou clique em PyPI (pack index)
