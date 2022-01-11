vetor = list()
for i in range(1, 11):
    while True:
        try:
            n = float(input(f'Digite o {i}° valor: '))
        except:
            print('Valor inválido! Digite novamente.')
            continue
        break
    vetor.append(n)
vetor.reverse()
print(vetor)