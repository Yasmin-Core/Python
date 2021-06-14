## Ano bissexto

print(' O ano é bissexto ou nao? BORA SABER ?! ')
ano= int(input('Digite o ano: '))
if (ano%4) == 0:
    if (ano%100) == 0:
        if (ano%400) == 0:
            print('BISSEXTO')
else:  
    print('Não é bissexto')