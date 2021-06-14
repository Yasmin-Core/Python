from random import randint
random= randint(0,10)
print(' Bem vindo ao jogo de adivinhação! ')
acertou= False
chances= 0
while not acertou:
    jogador= int(input(' Digite um número entre 0 e 10 que a máquina pensou: '))
    chances= chances +1
    if jogador == random:
        acertou= True
        print('Você precisou de {} chances para ACERTAR!'.format(chances))
print('FIM')
    


