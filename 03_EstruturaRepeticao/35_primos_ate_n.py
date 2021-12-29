while True:
    try:
        n = int(input('Digite até que valor testar: '))
    except:
        print('Valor inválido! Digite novamente.')
        continue
    if (n <= 1):
        print('O valor digitado deve ser um inteiro positivo maior que 1.')
        continue
    else:
        break
lista = []
for i in range(2, n):
    teste = True
    for c in range(2, i):
        if (i%c == 0):
            teste = False
        if (teste == True and c==i-1):
            lista.append(i)
print(f'Números primos de 1 até {n}: {lista}.')