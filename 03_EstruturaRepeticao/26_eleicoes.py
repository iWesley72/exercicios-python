try:
    nEleitores = int(input('Digite quantos eleitores participaram: '))
except:
    print('Valor inválido!')
    quit()
c1 = 0
c2 = 0
c3 = 0
for i in range(1, nEleitores+1):
    while True:
        voto = input(f'Digite em qual candidato(1, 2 ou 3) eleitor número {i} votou: ')
        if (voto == '1'):
            c1 += 1
            break
        elif (voto == '2'):
            c2 += 1
            break
        elif (voto == '3'):
            c3 += 1
            break
        else:
            print('Candidato inválido! Tente novamente.')
            continue
print(f'Total de votos do candidato 1: {c1}.')
print(f'Total de votos do candidato 2: {c2}.')
print(f'Total de votos do candidato 3: {c3}.')