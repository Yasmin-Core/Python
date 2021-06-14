# n é zero -> Pq vai comecar a contar a quantidade 
# de vezes que foi perguntado do zero , para nao contar o ultimo que é 999

# i é zero -> Pq vai começar a contar do indice 0 para nao contar o ultimo (999)

# soma é zero -> Pq a soma vai começar do indice 0

n = i = soma = 0
n= int(input('Digite um numero: '))

# Enquanto n for diferente de 999
while n != 999:
    # 0 + n -> somar os numeros digitados
    soma += n
    i += 1
    n= int(input('Digite um numero: '))
    
print('A quantidade de número que foi digitado é {}.'.format(i))
print ('A soma entre todos esses números é {}.'.format(soma))
print('---FIM---')
    

