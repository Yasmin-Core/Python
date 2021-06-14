somaidade= 0
mediaidade= 0
maioridadehomem= 0
nomevelho= ''
mulher20= 0
for p in range(1,5):
    print ('---- Analisador completo -----')
    print('-- Analisando o perfil da {} º pessoa --'.format(p))
    nome=  str(input('Nome: '))
    idade= int(input('Idade: '))
    sexo= str(input('Sexo (f/m): '))
    somaidade= somaidade + idade
    if p == 1 and sexo in 'mM':
        maioridadehomem= idade
        nomevelho= nome
    if sexo in "mM" and idade > maioridadehomem:
        maioridadehomem= idade
        nomevelho= nome
    if sexo in 'fF' and idade < 20:
        mulher20= mulher20 + 1
        
mediaidade= somaidade/4
print('A media da idade do grupo é {}.'.format(mediaidade))
print ('O homem mais velho tem {} anos e se chama {}.'. format(maioridadehomem, nomevelho))
print('Ao todo tem {} mulheres menores de 20 anos.'.format(mulher20))