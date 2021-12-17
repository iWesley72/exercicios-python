try:
    nota1 = float(input('Digite a primeira nota: '))
    nota2 = float(input('Digite a segunda nota: '))
except:
    print('Valor inválido!')
    quit()
media = (nota1 + nota2)/2
print('Média do aluno foi', round(media, 2))
if (media <= 6):
    if (media <= 4):
        print('Conceito E')
    else:
        print('Conceito D')
    print('Aluno reprovado')
else:
    if (media <= 7.5):
        print('Conceito C')
    elif (media <= 9):
        print('Conceito B')
    else:
        print('Conceito A')
    print('Aluno aprovado.')