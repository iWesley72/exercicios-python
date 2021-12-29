try:
    n = int(input('Digite o número a ser testado: '))
except:
    print('Valor inválido!')
    quit()
if (n <= 0):
    print('O número digitado deve ser um inteiro positivo!')
    quit()
else:
    for i in range(2, n):
        if (n % i == 0):
            print(f'{n} não é primo.')
            break
        if (i == n-1):
            print(f'{n} é primo.')