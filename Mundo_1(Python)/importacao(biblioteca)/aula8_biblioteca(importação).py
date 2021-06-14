## Para importar a biblioteca inteira 
#import (biblioteca)

## Para importa algo especifico da biblioteca
#from (biblioteca) import (especifico) 

## MATH (matematica) (biblioteca)
# ceil >> Arredondar o numero para cima 
# floor >>    "     ""       ""   baixo
# trunc >> Elimina os numeros da virgula para frente
# pow >> Semelhante ** (potencia)
# sqrt >> Raiz quadrada 
# factorial >> Fatorial

# Exemplo 
# >>> Raiz quadrada de um numero

import math
num= int(input(' Digite um numero: '))
raiz= math.sqrt (num)
#print ('A raiz de {} é igual a {}'.format(num, raiz))
                   #ou
# arredondar o resultado da raiz para cima 
print ('A raiz de {} é igual a {}'.format(num, math.ceil(raiz)))
