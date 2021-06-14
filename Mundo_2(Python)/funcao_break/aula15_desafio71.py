# Simulação de um banco eletrônico
# cedulas : R$ 50, 20, 10, 1

print('----------------------------------')
print('-=-=-=-= BANCO DA YASMIN -=-=-=-=-')
print('----------------------------------')
print(' ')
sacar= int(input('Qual o valor que você quer sacar ?: R$ '))
# O valor maior das cedulas
ced= 50
# contar a quantidade cedulas utilizadas
contcedula= 0

while True:
# Se o valor que a pessoa quer sacar for maior ou igual a 50
    if sacar >= ced:
        # o valor que a pessoas quer sacar menos R$ 50 , fazer isso ate nao ter mais como
        sacar -= ced
        # Contar a quantidade de cédula de R$50 foi preciso
        contcedula += 1
    else:
        # Se a quantidade de cedufor maior que zero
        if contcedula > 0:
            print(f'Total de {contcedula} cedulas de R$ {ced}.')
        # se a cedula for igual a 50 , ira utilizar cedulas de 20 reias
        if ced == 50:
            ced= 20
        elif ced == 20:
            ced= 10
        elif ced == 10:
            ced= 1
        # a cada looping contar a quantidade de cedula que precisa
        contcedula= 0
        if sacar == 0:
            break
print('****** VOLTE SEMPRE!! ********')




