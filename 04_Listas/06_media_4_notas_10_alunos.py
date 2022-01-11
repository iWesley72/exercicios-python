medias = []
for i in range(0, 10):
    notas = []
    print(f'\nAluno {i+1}:')
    for j in range(0, 4):
        while True:
            try:
                notas.append(float(input(f'Digite a {j+1}ª nota: ')))
            except:
                print('Nota inválida! Digite novamente.')
                continue
            break
    medias.append(sum(notas)/len(notas))
total = sum(i >= 7 for i in medias)
print(f'Total de alunos com média igual/superior a 7: {total}')