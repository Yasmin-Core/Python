import random
nome1= str(input('Escreva o nome do primeiro aluno: '))
nome2= str(input('Escreva o nome do segundo aluno:'))
nome3= str(input('Escreva o nome do terceiro aluno:'))
nome4= str(input('Escreva o nome do quarto aluno:'))
lista= (nome1, nome2, nome3, nome4)
sorteio= random.choice(lista)

print ('O aluno escolhido é: {}'.format(sorteio))
