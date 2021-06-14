frase= str(input(' Digite uma frase: '))
## split --> Separa cada palavra da frase
palavras= frase.split()
## join --> Junta tudo
junto= ''.join(palavras)
inverso= ''
## len --> Quantidade de caractere da frase
for letra in range (len(junto)-1, -1, -1):
    inverso += junto[letra]
print(junto, inverso)
if junto == inverso:
    print('È um PALÍNDROMO!')
else:
    print('Não é um PALÍNDROMO')