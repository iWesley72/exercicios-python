vetor = list()
for i in range(0, 5):
    while True:
        try:
            n = int(input('Digite o valor: '))
        except:
            print('Valor inválido! Digite novamente.')
            continue
        break
    vetor.append(n)
print(vetor)