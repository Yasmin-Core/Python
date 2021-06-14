print(' ===== BEM VINDO AO JOGO JOKENPÔ ======')
import random
print(''' ESCOLHA UMA DAS OPÇÕES
[1] Pedra
[2] Papel
[3] Tesoura''')
jogador= int(input('Qual é a sua opção?'))
print('A opção do jogador é {}'. format(jogador))
computador= random.randint(1,3)
print('A opção do computador é {} '.format(computador))

if computador == 1:
    if jogador == 1:
        print ('Ninguém venceu. Tente novamente!')
    elif jogador == 2:
        print ('Você VENCEU!')
    elif jogador == 3:
        print(' Você PERDEU!')
    else:
        print('Jogada INVÁLIDA!')
elif computador == 2:
    if jogador == 1:
        print ('Você PERDEU!')
    elif jogador == 2:
        print ('Ninguém venceu. Tente novamente!')
    elif jogador == 3:
        print(' Você VENCEU!')
    else:
        print('Jogada INVÁLIDA!')

elif computador == 3:
    if jogador == 1:
        print ('Você VENCEU!')
    elif jogador == 2:
        print ('Você PERDEU!')
    elif jogador == 3:
        print(' Ninguém venceu. Tente novamente')
    else:
        print('Jogada INVÁLIDA!') 

 