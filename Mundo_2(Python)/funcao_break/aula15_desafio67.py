# while, for e break

# While true -> looping infinito
while True:
    print('----Tabuada----')
    n= int(input('Digite um numero para saber a tabuada dele: '))
    # Se o numero digitado for negativo o looping se encerra (break)
    if n < 0:
        break
    #para contar no intervalo de (1 ao 11)
    for c in range (1,11) :
    #Ex: 1 x 1 = 1*1
        print(f'{n} x {c} = {n*c}')
# Quando o looping parar ira aparecer isso 
print(' ENCERROU!')

