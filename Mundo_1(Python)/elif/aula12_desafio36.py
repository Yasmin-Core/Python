casa= float(input('Qual o valor da casa ? R$ '))
salário= float(input('Qual é o seu salário? R$ '))
anos= int(input('Em quantos anos você pretende pagar o empréstimo?'))
a= casa /(anos*12)
mínimo= salário * 30/100
print(mínimo)
if a >= mínimo:
    print('Empréstimo NEGADO')
else:
    print('Empréstimo ACEITO')