#Sequencia de fibonacci -> serão a soma dos dois números anteriores
print('***** Sequencia de Fibonacci******')
n= int(input('Quantos numeros voce quer que mostre na sequencia de fibonacci?:'))

# A sequencia de fibonacci sempre começa com zero e um
i1 = 0
i2 = 1
print('{} -> {} -> '.format(i1, i2), end='')
# Entao o contador vai comerça conta a partir do indice 3
i = 3

#Enquanto o indice for menor que 'n' 

while i <= n:
    #O indice 3 vai ser sempre 0 + 1
    i3 = i1 + i2 
    print('{} -> '.format(i3), end='')
    # O indice 1 vai ser igual o indice dois - 0 -> 1 -> 1
    i1 = i2
    # O indice 2 vai ser igual o indice 3 - 0 -> 1 -> 1 -> (1+1) 2
    i2 = i3
    i += 1
print('fim')