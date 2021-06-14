velocidade= float(input('Digite a velocidade que vocẽ passou no radar: '))
if velocidade <= 80:
    print('Você nâo foi multado!')
else:
    print(' Você foi MULTADO!')
    valor= (velocidade - 80) * 7
    print( ' O valor da multa é R${}'.format(valor))