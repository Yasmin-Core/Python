print(' ---- PA ----')
termo= int(input('Digite o primeiro termo: '))
razão= int(input('Digite a razão: '))

cont= 1
while cont <= 10:
    print('{}->'.format(termo), end= '')
    termo= termo + razão
    cont += 1
print('FIM')

