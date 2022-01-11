notas = list()
for i in range(1,5):
    while True:
        try:
            nota = float(input(f'Digite a {i}ª nota: '))
        except:
            print('Nota inválida! Digite novamente')
            continue
        break
    notas.append(nota)
media = sum(notas)/len(notas)
print(f'Nota 1: {notas[0]}')
print(f'Nota 2: {notas[1]}')
print(f'Nota 3: {notas[2]}')
print(f'Nota 4: {notas[3]}')
print(f'Média Geral: {media}')