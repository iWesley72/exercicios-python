alturas = list()
idades = list()
for i in range(0, 5):
    while True:
        try:
            idade = int(input(f'Idade(anos) {i+1}ª pessoa: '))
        except:
            print('Idade inválida! Tente novamente.')
            continue
        if (idade < 0):
            print('Idade inválida! Tente novamente.')
            continue
        break
    while True:
        try:
            altura = float(input(f'Altura(m) {i+1}ª pessoa: '))
        except:
            print('Altura inválida! Tente novamente.')
            continue
        if (altura <= 0):
            print('Altura inválida! Tente novamente.')
            continue
        break
    idades.append(idade)
    alturas.append(altura)
idades.reverse()
alturas.reverse()
print(f'Vetor idade invertido: \n{idades}')
print(f'Vetor altura invertido: \n{alturas}')