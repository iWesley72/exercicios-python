print('**TABUADA**')
try:
    valor = int(input('Digite o número que você quer a tabuada: '))
except:
    print('Valor inválido.')
    quit()
print('Tabuada de ' + str(valor) + ':')
for i in range(1, 11):
    print(valor, 'X', i, '=', valor*i)