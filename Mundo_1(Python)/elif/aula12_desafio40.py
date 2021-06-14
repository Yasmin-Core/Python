nota1= float(input('Digite uma nota: '))
nota2= float(input('Digite a segunda nota: '))
a= (nota1 + nota2) / 2
if a >= 7.0:
    print(' APROVADO ')
elif a < 5.0:
    print (' REPROVADO ')
elif 7 > a >= 5:
    print(' RECUPERAÇÃO ')

