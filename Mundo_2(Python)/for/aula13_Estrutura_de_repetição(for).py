## Exemplo na prática (FOR)

# Repetir o 'oi' cinco vezes

for c in range (1,6):
    print('oi')
print('fim')

# Contar do zero até o cinco

for c in range (0,6):
    print(c)
print('fim')

# Contagem regressiva do seis até o um

for c in range (6,0,-1):
    print(c)
print('fim')

# Contar um numero qualquer

n= int(input('Digite um número: '))
for c in range (0,n):
    print(c)
print ('FIM')

# Fazendo a contagem pulando de um numero qualquer

i= int(input('Inicio: '))
f= int(input('Fim: '))
p= int(input('Passo: '))
for c in range (i, f+1, p):
    print(c)
print('fim')

# Digitar algo várias vezes

for c in range (0,3):
    n= int(input('Digite um valor:'))
print('fim')