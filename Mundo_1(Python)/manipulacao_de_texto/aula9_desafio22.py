# Maiuscula
# Minuscula
# Quantidade de letras
# Quantidade de letras (primeiro nome)

nome= str(input('Escreva o seu nome inteiro: '))

nome= nome.upper()
nome2= nome.lower()
nome3= (len(nome)-nome.count(' '))
nome4= nome.find(' ')

print('Em maiuscula: {}'.format(nome))
print('Em minuscula: {}'.format(nome2))
print('Quantidade de letra: {}'.format(nome3))
#            ou
#print('Quantidade de letra: {}'.format(len(nome)-nome.count(' ')))
print('O seu primeiro nome tem {} letras'.format(nome4))



