while True:
    try:
        x = int(input('Até que valor deseja a sequência: '))
    except:
        print('Valor inválido!')
        continue
    break
h = 0
sequencia = 'H = '
for i in range(1, x+1):
    n = i
    sequencia += '1/'+str(n)+' '
    h += 1/n
    if (i != x):
        sequencia += '+ '
print(sequencia)
print(f'H = {h}')