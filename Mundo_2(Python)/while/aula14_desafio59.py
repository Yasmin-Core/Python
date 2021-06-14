a= int(input('Digite um valor inteiro:'))
b= int(input('Digite outro valor inteiro:'))
resposta= 0
while resposta != 5:
    print( '''O que voce deseja fazer com esse numero: 
[1] Somar  
[2] Multiplicar 
[3] Maior
[4] Digitar novos números 
[5] Sair do programa''')
    resposta= int(input('Escolhe as opçoes:'))
    if resposta == 1:
        soma= a+b
        print('A soma entre esses dois numeros é {}.'.format(soma))
    elif resposta == 2:
        multiplicar= a * b
        print('A multiplicação entre esse dois numeros é {}.'.format(multiplicar))
    elif resposta == 3:
        if a > b:
            print('O valor maior é o {}.'.format(a))
        if b > a:
            print('O valor maior é o {}.'.format(b))
    elif resposta == 4:
        print(' Digite os numeros novamente')
        a= int(input('Digite um valor inteiro:'))
        b= int(input('Digite outro valor inteiro:'))
    elif resposta == 5:
        print('Finalizando...')
    else:
        print('Opção invalida. Tente novamente!')
print ('*** Fim ***')