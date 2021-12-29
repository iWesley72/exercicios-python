try:
    base = int(input('Digite a base da potência: '))
    expoente = int(input('Digite o expoente da potência: '))
except:
    print('Valor inválido!')
    quit()
if (expoente < 0):
    print('O expoente não pode ser um valor negativo!')
elif (expoente == 0):
    print(base,'elevado a', expoente, 'é 1.')
else:
    total = 1
    for i in range(1, expoente + 1):
        total *= base
    print(base, 'elevado a', expoente, 'é igual', total)
