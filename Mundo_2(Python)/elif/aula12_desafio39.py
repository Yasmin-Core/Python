ano= int(input('Digite o seu ano de nascimento: '))
if ano == 2003:
    print ('Essa é a hora certa para se alistar!')
elif ano < 2003:
    print ('Você ainda esta a tempo de alistar')
    a= 2003-ano
    print ('Falta {} anos para vocẽ se alistar!'.format(a))
elif ano > 2003:
    print ('Você está atrasado para se alistar!')
    b= ano - 2003
    print('Você esta atrasado a {} ano(s).'.format(b))