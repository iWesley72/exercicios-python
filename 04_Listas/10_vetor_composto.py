vetorA = list()
vetorB = list()
vetorC = list()
for i in range(0, 20):
    n = input(f'Digite o {i+1}° elemento: ')
    if (i < 10):
        vetorA.append(n)
    else:
        vetorB.append(n)
for i in range(0, 10):
    vetorC.append(vetorA[i])
    vetorC.append(vetorB[i])
print(f'Vetor A: {vetorA}')
print(f'Vetor B: {vetorB}')
print(f'Vetor C: {vetorC}')