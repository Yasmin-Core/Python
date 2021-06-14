distancia= float(input(' Qual é a distância da sua viagem?: '))
if distancia <= 200:
    valor1 = (distancia) * 0.50
    print(' O valor da sua viagem é R$ {}.'.format(valor1))

else:
    valor2 = (distancia) * 0.45
    print(' O valor da sua viagem é R$ {}.'.format(valor2))