alunos = []
totalCodigos = 0
while True:
    try:
        codigo = int(input('Código do aluno: '))
    except:
        print('Valor inválido! Tente novamente.')
        continue
    if (codigo == 0):
        break
    else:
        while True:
            try:
                altura = float(input('Altura do aluno(m): '))
                peso = float(input('Peso do aluno(kg): '))
            except:
                print('Valor inválido! Tente novamente.')
                continue
            break
        totalCodigos += 1
        alunos.append(codigo)
        alunos.append(altura)
        alunos.append(peso)
#testar altura
totalAltura = 0
maiorAltura = 0
codigoAltura = 0
for i in range(1, len(alunos) + 1, 3):
    totalAltura += alunos[i]
    if (maiorAltura == 0):
        maiorAltura = alunos[i]
        codigoAltura = alunos[i-1]
    elif (maiorAltura < alunos[i]):
        maiorAltura = alunos[i]
        codigoAltura = alunos[i-1]
#testar peso
totalPeso = 0
maiorPeso = 0
codigoPeso = 0
for i in range(2, len(alunos) + 1, 3):
    totalPeso += alunos[i]
    if (maiorPeso == 0):
        maiorPeso = alunos[i]
        codigoPeso = alunos[i-2]
    elif (maiorPeso < alunos[i]):
        maiorPeso = alunos[i]
        codigoPeso = alunos[i-2]
print(f'Maior altura: {maiorAltura} m. É o aluno de código {codigoAltura}.')
print(f'Média altura de todos alunos: {round(totalAltura/totalCodigos, 2)} m')
print(f'Maior peso: {maiorPeso} kg. É o aluno de código {codigoPeso}')
print(f'Média peso de todos alunos: {round(totalPeso/totalCodigos, 2)} kg')