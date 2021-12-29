try:
    n = int(input('Fatorial de : '))
except:
    print('Valor inválido!')
    quit()
msg = str(n) + '! = '
valor = 1
for i in range(n, 0, -1):
    if (i == n):
        msg += str(n) + ' '
    else:
        msg += '. ' + str(i) + ' '
    valor *= i
msg += '= ' + str(valor)
print(msg)