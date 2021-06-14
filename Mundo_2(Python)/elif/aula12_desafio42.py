a= float(input('Digite o comprimento de uma reta:'))
b= float(input('Digite o comprimento de uma reta:'))
c= float(input('Digite o comprimento de uma reta:'))

if a<b+c and b<a+c and c<a+b:
    print('Essas 3 retas formam um TRIANGULO')
    if a==b==c:
        print ('Esse triângulo é um EQUILÁTERO')
    elif a != b != c != a:
        print ('Esse triângulo é um ESCALENO')
    else:
        print('Esse triãngulo é um ISÓSCELES')
else: 
    print('Essas retas não formam um triangulo. Tente novamente!.')