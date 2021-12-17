from math import floor
try:
    valor = int(input('Digite quanto você deseja sacar: R$ '))
except:
    print('Valor inválido!')
    quit()
notas100 = floor(valor/100)
notas50 = floor((valor - notas100*100)/50)
notas10 = floor((valor - notas100*100 - notas50*50)/10)
notas5 = floor((valor - notas100*100 - notas50*50 - notas10*10)/5)
notas1 = floor((valor - notas100*100 - notas50*50 - notas10*10 - notas5*5))

if (valor < 10 or valor > 600):
    print('Valores para saque devem ser de R$10,00 até R$600,00.')
else:
    print('Notas de R$100:', notas100)
    print('Notas de R$50:', notas50)
    print('Notas de R$10:', notas10)
    print('Notas de R$5:', notas5)
    print('Notas de R$1:', notas1)