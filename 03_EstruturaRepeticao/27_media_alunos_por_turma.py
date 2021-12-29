from math import ceil
try:
    qtdTurmas = int(input('Digite quantas turmas existem: '))
except:
    print('Valor inválido!')
    quit()
qtdAlunos = 0
for i in range(1, qtdTurmas+1):
    while True:
        try:
            qtdAlunos += int(input(f'Digite quantos alunos tem na turma {i}: '))
        except:
            print('Valor inválido!')
            continue
        break
media = round(qtdAlunos/qtdTurmas)
print(f'Média de {media} alunos por turma.')
if(media > 40):
    n = (media - 40)*qtdTurmas
    qtdTurmasNovas = ceil(n/40)
    print(f'É necessário abrir {qtdTurmasNovas} turmas, para que o limite de 40 alunos por turma seja respeitado!')