altura = list()
idade = list()

for i in range(0, 30):
    while True:
        try:
            alturaAluno = float(input(f'Altura do {i+1}° aluno: '))
            idadeAluno = int(float(input(f'Idade do {i+1}° aluno: ')))
        except:
            print('Valor inválido! Digite novamente.')
            continue
        altura.append(alturaAluno)
        idade.append(idadeAluno)
        break

mediaAltura = sum(altura)/len(altura)
contador = 0
for i in range(0, 30):
    if (altura[i] < mediaAltura and idade[i] > 13): contador += 1

print(f'Total de alunos com mais de 13 anos e altura abaixo da média: {contador}')