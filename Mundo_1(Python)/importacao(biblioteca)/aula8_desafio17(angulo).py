## Biblioteca: math.hypot
# calcular a hipotenusa

co= float(input('Digite o comprimento do cateto oposto:'))
ca= float(input('Digite o comprimento do cateto adjacente:'))
#hi= (co**2+ca**2)**(1/2)
#          ou
import math
hi= math.hypot (co,ca)
print ('A hipotenusa vale {:.2f}'.format(hi))
