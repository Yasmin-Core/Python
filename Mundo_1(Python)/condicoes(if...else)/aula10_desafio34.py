
salario= float(input(' Digite o seu salário: '))
if (salario) >= (1250.00):
    novo= salario + (salario * 10/100)
    print('O seu salario teve um aumento de 10%, e com isso , passou a ser R$ {}.'.format(novo))
if (salario) <= (1250.00):
    novo1= salario + (salario * 15/100)
    print('O seu salario teve um aumento de 15%, e com isso , passou a ser R$ {}.'.format(novo1))