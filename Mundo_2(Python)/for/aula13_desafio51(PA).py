print ( '----- Progressão Aritmética-----')
primeiro= int(input('Digite o primeiro termo:'))
razão= int(input('Digite a razão: '))
decimo= primeiro + (11-1) * razão
for c in range (primeiro, decimo, razão):
    print('{}'.format(c), end='-')
