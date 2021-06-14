# Importar a biblioteca randon para gera numeros 
import random

# variavel para contar as vitorias do jogo
v= 0
# looping infinito
while True:
    print("-=-=-= BEM VINDO AO JOGO DE UMPAR OU PAR -=-=-=")
    n= int(input(' Digite um numero entre 0 e 10:'))
    #gera numeros aleatorios de 1 ao 10
    computador= random.randint (0,10)
    # a soma do numero que a pessoa digitou com o numero que o computador gerou
    total= n + computador
    pi= str(input(' PAR ou IMPAR [p/i]: '))
    print(f"O total foi {total}, e o computador foi {computador}")
    # escrever " Deu PAR" se for PAR, senão " Deu IMPAR"
    print(' Deu PAR' if total % 2 == 0 else 'Deu IMPAR')
    # Se "pi" for par
    if pi == 'p':
        # e o total tambem , o jogador venceu
        if total % 2 == 0 :
            print(' VOCÊ VENCEU !!!!')
            v+=1
            print(' ---- Vamos jogar novamente ! ----')
        # Senão, o jogador perdeu
        else:
            print(' VOCE PERDEU !')
            break
    # Se o 'pi' for impar
    elif pi == 'i':
        # e o total tambem , o jogador venceu
        if total % 2 == 1:
            print(' VOCÊ VENCEU !!!!')
            v+=1
            print(' ---- Vamos jogar novamente ! ----')
        #Senão, o candidato perdeu
        else:
            print(' VOCE PERDEU !')
            break
print(f' GAME OVER ! Voce venceu {v} vezes !')



