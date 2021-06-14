produto= float(input(' O valor do produto: R$ '))
print ('''===== FORMAS DE PAGAMENTOS ======
[1] á vista dinheiro/cheque
[2] á vista no cartão
[3] 2 X no cartão
[4] 3 X ou mais no cartão''')
opção = int(input('Qual é a opção?'))

if opção == 1 :
    a= produto - (produto * 10 / 100)
    print('Você irá pagar neste produto R${:.2f}, pois teve um desconto de 10%.'.format(a))
elif opção == 2 :
    b= produto - (produto * 5 / 100)
    print('Você irá pagar neste produto R${:.2f}, pois teve um desconto de 5%.'.format(b))
elif opção == 3 : 
    print('Você irá pagar neste produto R${:.2f}, pois não teve nenhum desconto.'.format(produto))
elif opção == 4 :
    c= produto + (produto * 20 / 100)
    print('Você irá pagar neste produto R${:.2f}, pois teve 20% de juros.'.format(c))