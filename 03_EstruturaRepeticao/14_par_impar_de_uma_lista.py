pares = 0
for i in range(1, 11):
    try:
        num = int(input('Digite algum valor inteiro: '))
    except:
        print('Valor inválido!')
        quit()
    if (num%2 == 0):
        pares += 1
print('Total de', pares, 'números pares.')
print('Total de', 10 - pares, 'números impares.')