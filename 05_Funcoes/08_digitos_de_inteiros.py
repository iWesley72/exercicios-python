def digitosDeInteiro(n):
    try:
        int(n)
    except:
        print('Valor não é um número inteiro!')
        return
    if (int(n) < 0):
        print(len(n)-1, 'digitos.')
    else:
        print(len(n), 'digitos.')

valorTeste = input('Valor a ser testado: ')
digitosDeInteiro(valorTeste)