notas = []
while True:
    nome = input('Atleta: ')
    if (nome == ''):
        break
    else:
        for i in range(1, 8):
            while True:
                try:
                    notas.append(float(input(f'{i}ª nota: ')))
                except:
                    print('Valor inválido! Digite novamente.')
                    continue
                break
        maiorNota = max(notas)
        menorNota = min(notas)
        notas.remove(maiorNota)
        notas.remove(menorNota)
        media = sum(notas)/5
        print(f'\nResultado final:')
        print(f'Atleta: {nome}')
        print(f'Melhor nota: {maiorNota}')
        print(f'Pior nota: {menorNota}')
        print(f'Média: {round(media, 2)}')
