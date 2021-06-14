from datetime import date
atual= date.today().year
for p in range (1,8):
    nasc= int(input('Digite o ano de nascimento da {}º pessoa: '.format(p)))
    idade= atual - nasc
    if idade >= 21:
        print( 'Essa pessoa é MAIOR')
    else:
        print( 'Essa pessoa é MENOR')
