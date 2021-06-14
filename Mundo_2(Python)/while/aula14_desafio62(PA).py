print('--- PA ---')
termo= int(input('Digite o primeiro termo: '))
razão= int(input('Digite a razão: '))
cont = 1
total= 0
mais= 10
while mais != 0:
    total= total + mais
    while cont <= total:
        print('{} -> '.format(termo), end='')
        termo= termo + razão
        cont = cont + 1
    print(' Pausa ')   
    mais = int(input('Quantos termos você desejar saber mais?: '))
    