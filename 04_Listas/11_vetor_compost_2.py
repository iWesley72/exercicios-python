vetorA = list()
vetorB = list()
vetorC = list()
for i in range(0, 20):
    n = input(f'Digite o {i+1}° elemento: ')
    if (i < 10):
        vetorA.append(n)
    else:
        vetorB.append(n)

for i in range(2, 12, 3):
    for c in range(i-2, i+1):
        try:
            vetorC.append(vetorA[c])
        except:
            continue
    for e in range(i-2, i+1):
        try:
            vetorC.append(vetorB[e])
        except:
            continue

print(f'Vetor A: {vetorA}')
print(f'Vetor B: {vetorB}')
print(f'Vetor C: {vetorC}')