# Contar :
# A) Quantas pessoas tem mais de 18 anos (i)
# b) Quantos homens cadastrados (h)
# C) Quantas mulheres tem menor de 20 anos (m) 
h= m= i= 0

# looping infinito

while True:
    print('=-=-=- Dados =-=-=-=')
    idade= int(input('Quantos anos você tem: '))
    sexo= str(input('Qual é o seu sexo[f/m]: '))
    d= str(input('Voce deseja continuar? [s/n]: '))
    # SE a idade for maior ou igual a 18, conte mais 1
    if idade >= 18:
        i+= 1
    # SE o sexo for masculino (m), conte mais 1
    if sexo == 'm':
        h+= 1
    # SE o sexo for feminino (f) e a idade for menor que 20 anos, conte mais 1
    if sexo == 'f' and idade < 20:
        m+= 1
    # SE a resposta da pessoa for NÃO (n) , o programa para (break)
    if d == 'n':
        print('PAROU')
        break
print(f'{i} pessoas tem mais de 18 anos. Contem {h} homens. Existe {m} mulheres menores de 20 anos.')
