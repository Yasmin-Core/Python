media = maior = menor = n = soma= 0
n= int(input('Digite um numero:'))
d= str(input('Voce deseja continuar (s/n)? : '))
i = 1

# Enquanto 'd' for 's' = sim
while d in 's':
   n= int(input('Digite um numero:')) 
   # soma os numeros que estao sendo digitados
   soma += n
   i += 1
# Se obter só um indice , este indice vai ser o maior e o menor numero
   if i == 1:
       maior = menor = n
# Senão 
# Descobrir qual  numero é maior e qual é o numero menor
   else:
    if n > maior:
        n = maior
    if n < menor:
        n= menor
    d= str(input('Voce deseja continuar (s/n)? : '))

media= soma / 2
print ('A média entre esses numeros são: {}'.format(media))
print('Você digitou {} numeros.'. format(i))
     
    

    