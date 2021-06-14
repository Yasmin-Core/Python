#Qual é o total da compra (s -> soma)
#Quantos produtos custam mais de 1000.00 (p)
# Qual é o nome do produto mais barato (c e o barato)

s=0
p=0
c=1
barato= ' '

while True:
    nome= str(input('Qual é o nome do produto?: '))
    produto= float(input('Quanto custa esse produto?: '))
    sn= str(input('Voce desejar continuar [s/n]: '))
    # somar os preços dos produtos
    if produto >0:
        s+=produto
    # Contar a quantidade produto que custa mais de 1000.00
    if produto > 1000:
        p+=1
    # Se o indice 1 for o mais barato
    if c == 1:
        menor= produto
        barato= nome
    #Senão
    else:
        if produto < menor:
            menor= produto
            barato= nome
    # Se a resposta for "n"(não), Break
    if sn == 'n':
        break
    
print('-------------------------------')
print(f"O total gasto nessa compra é de R$ {s} ")
print(f'Teve {p} quantidade de produtos que custava mais de R$ 1000.00') 
print(f'O produto {barato} custava R$ {menor}, e foi o produto mais barato da compra.')