peso= float(input(' Qual é o seu peso? '))
altura= float(input(' Qual é a sua altura? '))
imc= peso/(altura ** 2)
if imc <= 18.5:
    print(' Você está a BAIXO DO PESO!.')
elif 18.5 <= imc < 25:
    print(' Você está com o PESO IDEAL!.')
elif 25 <= imc < 30:
    print(' Você está com SOBREPESO!.')
elif 30 <= imc < 40:
    print(' Voce está OBESO!.')
elif imc > 40:
    print (' Você esta com OBESIDADE MÓRBIDA!.')


