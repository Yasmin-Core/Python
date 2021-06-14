from math import factorial
n= int(input('Digite um numero para descobrir o fatorial dele: '))
f= factorial(n)
c = n
f = 1
print('Calculando {}!= '.format(c), end='')
while c >0:
    print('{}'.format(c), end='' )
    print(' x ' if c > 1 else ' = ', end='')
    f = f * c
    c = c-1
print ('{}'. format(f))

