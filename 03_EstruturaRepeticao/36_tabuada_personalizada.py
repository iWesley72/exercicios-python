# m1 -> valor inicial, mx-> valor final
while True:
    try:
        n = int(input('Montar a tabuada do: '))
        m1 = int(input('Começar por: '))
        mx = int(input('Terminar em: '))
    except:
        print('Valor inválido! Digite novamente.')
        continue
    if(m1 > mx):
        print('O valor inicial deve ser menor que o final.')
        continue
    else:
        break
print(f'Vou montar da tabuada do {n} começando em {m1} e terminando em {mx}:')
for i in range(m1, mx+1):
    print(f'{n} X {i} = {n*i}')