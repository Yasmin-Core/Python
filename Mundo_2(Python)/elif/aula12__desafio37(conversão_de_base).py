print('==== BASE DE CONVERSÃO ====')
número= int(input('Digite um número inteiro: '))
print('''==== TIPOS DE BASE DE CONVERSÃO ====
[1] Binário
[2] Octal
[3] Hexadecimal''')
opção= int(input('Qual é a opção? '))
if opção == 1:
    print('O número {} convertido em BINÁRIO é {}.'.format(número, bin(número)))
elif opção == 2:
    print('O número {} convertido em OCTAL é {}.'.format(número, oct(número)))
elif opção == 3:
    print('O número {} convertido em HEXADECIMAL é {}.'.format(número, hex(número)))
else:
    print('Opção inválida. Tente novamente!')

