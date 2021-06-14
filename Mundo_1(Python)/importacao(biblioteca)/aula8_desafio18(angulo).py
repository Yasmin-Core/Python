## Biblioteca: math.cos, sin, tan

angulo= float(input('Digite o ângulo: '))
import math
cos= math.cos(math.radians(angulo))
print('O cosseno desse angulo é: {:.2f}'.format(cos))
sen= math.sin(math.radians(angulo))
print('O seno desse angulo é: {:.2f}'.format(sen))
tan= math.tan(math.radians(angulo))
print('A tangente desse angulo é: {:.2f}'.format(tan))
