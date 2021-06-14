a= float(input('Digite o comprimento de uma reta:'))
b= float(input('Digite o comprimento de uma reta:'))
c= float(input('Digite o comprimento de uma reta:'))

if a<b+c and b<a+c and c<a+b:
    print('Essas 3 retas formam um TRIANGULO')
else:
    print('Essa 3 retas NÃo formam um triangulo')