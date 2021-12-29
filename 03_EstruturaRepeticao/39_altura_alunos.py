maiorAltura = 0
menorAltura = 0
codMenorAltura = 0
codMaiorAltura = 0
for i in range(1, 11):
    while True:
        try:
            numero = int(input('Número do aluno: '))
            altura = float(input('Altura do aluno(m): '))
        except:
            print('Valor inválido! Tente novamente.')
            continue
        break
    if (maiorAltura == 0):
        maiorAltura = altura
        codMaiorAltura = numero
    elif (maiorAltura < altura):
        maiorAltura = altura
        codMaiorAltura = numero

    if (menorAltura == 0):
        menorAltura = altura
        codMenorAltura = numero
    elif (menorAltura > altura):
        menorAltura = altura
        codMenorAltura = numero
print(f'Aluno número {codMaiorAltura} é o mais alto, com {maiorAltura} m.')
print(f'Aluno número {codMenorAltura} é o mais baixo, com {menorAltura} m.')