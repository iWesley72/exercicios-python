while True:
    try:
        x = int(input('Até qual termo você deseja a sequência? '))
    except:
        print('Valor inválido!')
        continue
    break
sequencia = ''
s = 0
for i in range(1, x+1):
    n = 1 +(i-1)
    m = 1+2*(i-1)
    s += n/m
    sequencia += str(n)+'/'+str(m)+' '
    if (i != x):
        sequencia += '+ '
print(f'S = {sequencia}')
print(f'S = {s}')