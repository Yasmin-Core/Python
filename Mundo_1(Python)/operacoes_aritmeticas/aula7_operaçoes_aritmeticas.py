## Operaçoẽs aritmeticas
# + ADIÇÃO,  - SUBTRAÇÃO, * MULTIPLICAÇÃO, / DIVISÃO, 
# ** POTÊNCIA, // DIVISÃO INTEIRA, % RESTO DA DIVISÃO 

## Ordem de precedencia 
# 1 ()
# 2 **
# 3 *, /, // e %
# 4 + e - 

# Exercicios
n1= int(input('Um valor:'))
n2= int(input('Outro valor:'))
a= n1+n2
s= n1-n2
m= n1*n2
d= n1/n2
p= n1**n2
di= n1//n2
rd= n1%n2

print('A soma é {}, a subtração é {}, a multipĺicação é {}, a divisão é {},'.format (a, s, m, d))
print('a potência é {},a divisão inteira é {},e o resto da divisão é {}.'.format(p, di, rd))



