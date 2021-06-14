# WHILE (enquanto)

a= str(input('Digite o seu sexo:')).strip().upper()[0]
while a not in 'FMfm':
    a= str(input('Dados invalidos. Digite novamente o seu sexo:')).strip().upper()[0]
print('O sexo {} foi REGISTRADO!'.format(a))

## strip >> Remove todos os espaços do começo e do final da frase
## upper >> Maiúscula