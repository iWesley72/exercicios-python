while True:
    saltos = []
    nome = input('Atleta: ')
    if (nome == ''): break
    while len(saltos) < 5:
        try:
            saltos.append(float(input(f'{len(saltos)+1}° salto: ')))
        except:
            print('Valor inválido! Tnete novamente.')
            continue
    print(f'Atleta: {nome}')
    print(f'Saltos: {saltos}')
    print(f'Média dos saltos: {sum(saltos)/len(saltos)}')