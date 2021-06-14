## Maior e menor valor

numero1= int(input('Digite o primeiro numero: '))
numero2= int(input('Digite o segundo numero: '))
numero3= int(input('Digite o terceiro numero: '))

# verificando o numero menor

menor= numero1
if numero2 < numero1 and numero2 < numero3:
    menor = numero2
if numero3 < numero1 and numero3 < numero2:
    menor = numero3

# Verificando o numero maior

maior= numero1
if numero2 > numero1 and numero2 > numero3:
    maior= numero2
if numero3 > numero1 and numero3 > numero2:
    maior= numero3
print('O menor numero digitado foi {}'.format(menor))
print('O maior numero digitado foi {}'.format(maior))