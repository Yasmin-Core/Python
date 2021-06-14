## Utilizando a função BREAK - interropendo os looping

# s -> soma
s=0
# contador / indice -> coemça a contar do -1 para nao contar o 999( numero de parada )
c= -1
# Enquanto for verdadeiro ( looping infinito)
while True:
    n= int(input('Digite um numero: '))
    # Conta +1
    c += 1
    if n == 999:
        # Quebra o looping
        break
    # Soma os numeros respondidos
    s+=n
print(f'Foram digitados {c} e a soma entre eles são {s}')
