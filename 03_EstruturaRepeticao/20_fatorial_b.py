while True:
    try:
        n = int(input('Digite o valor que você deseja saber o fatorial: '))
    except:
        print('\nValor inválido!\n')
        n = 0
    if (n <= 0 or n >= 16):
        print('O valor deve ser um número inteiro positivo entre entre 0 16!\n')
    elif(0<n<16):
        fatorial = 1
        for i in range(1, n + 1):
            fatorial *= i
        print(f'Fatorial de {n} é {fatorial}.\n')
    