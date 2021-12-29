while True:
    valor = int(input('Digite um número entre 0 e 10: '))
    if (0<=valor<=10):
        print('Valor válido!')
        break
    else:
        print('Valor inválido, tente novamente.')