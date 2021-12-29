try:
    n = int(input('Digite até que valor você quer testar: '))
except:
    print('Valor inválido!')
    quit()
for i in range(2, n):
    testador = False
    for j in range(2, i):
        if (i % j == 0):
            testador = True
        elif (j == i-1 and testador == False):
            print(f'{i} é um número primo!')
    