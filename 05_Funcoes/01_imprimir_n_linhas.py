def imprimirLinha(n):
    for i in range(1, n+1):
        print((str(i) + ' ')*i)

linhas = int(input('Quantas linhas você deseja imprimir? '))
print('')
imprimirLinha(linhas)