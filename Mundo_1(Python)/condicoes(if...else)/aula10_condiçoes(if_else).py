## Exemplo 1

tempo= (int(input('Quantos anos tem o seu carro ?')))
if tempo <=3:
   print('Carro novo')
else:
    print('Carro velho')

## Exemplo 2

n1= float(input('Digite a primeira nota: '))
n2= float(input('Digite a segunda nota: '))
m= (n1+n2)/2
print('A sua média foi {:.1f}'.format(m))
if m > 6.0:
    print(' A sua média foi boa! PARABENS!')
else:
    print('A sua média foi ruim!. Estude mais!')



