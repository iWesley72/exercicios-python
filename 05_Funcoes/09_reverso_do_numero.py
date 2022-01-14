def inverterInteiro(n):
    try:
        int(n)
    except:
        print('Valor informado não é um inteiro!')
        return
    return n[::-1]

valorTeste = input('Valor a ser invertido: ')
inverterInteiro(valorTeste)