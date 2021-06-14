from random import randint
random= randint(0,5)
print(' Bem vindo ao jogo de adivinhação! ')
numero= float(input(' Digite um número entre 0 e 5 que a máquina pensou: '))

if numero == random:
    print(' Você venceu !!!')
else:
    print(' Voce perdeu -_-')
