try:
    n = int(input('Digite o número a ser testado: '))
except:
    print('Valor inválido!')
    quit()
if (n <= 0):
    print('O número digitado deve ser um inteiro positivo!')
    quit()
else:
    contador = 0
    for i in range(2, n):
        if (n % i == 0):
            if (contador == 0):
                print(f'{n} não é primo, é divisível por ', end='')
            elif (contador > 0):
                print(i, end=' ')
            contador += 1
        if (i == n-1 and contador == 0):
            print(f'{n} é um número primo.')