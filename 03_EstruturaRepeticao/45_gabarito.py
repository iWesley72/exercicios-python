from typing import Container


gabarito = 'abcdeedcba'
respostas = ''
maiorAcerto = 0
menorAcerto = 0
mediaGeral = 0
nAlunos = 0
while True:
    if (nAlunos == 0):
        for i in range(1, 11):
            respostas += input(f'Resposta questão {i}: ').lower()
        nAlunos += 1
    else:
        pergunta = input('Mais algum aluno irá responder? (S/N): ')
        if (pergunta == 's'):
            for i in range(1, 11):
                respostas += input(f'Resposta questão {i}: ').lower()
            nAlunos += 1
        elif (pergunta == 'n'):
            break
        else:
            print('Responda com s - sim ou n - não.')
            continue
    acertos = sum(i == j for i, j in zip(respostas, gabarito))
    mediaAluno = acertos/10
    mediaGeral += acertos/nAlunos
    if (maiorAcerto == 0):
        maiorAcerto = acertos
    elif (maiorAcerto < acertos):
        maiorAcerto = acertos
    if (menorAcerto == 0):
        menorAcerto = acertos
    elif (menorAcerto > acertos):
        menorAcerto = acertos
print(f'Maior acerto: {maiorAcerto}')
print(f'Menor acerto: {menorAcerto}')
print(f'Total de alunos que utilizaram o sistema: {nAlunos}')
print(f'Média das notas da turma: {round(mediaGeral, 2)}')
    