# Em uma matriz 3x3 onde seus elementos são valores de 1 a 9, a soma de todos os elemento é 45, o que permite um valor máximo de 15 por linha, isto se não houver repetição entre elementos da matriz. (Válido apenas para matriz 3x3)

from itertools import permutations

def combinacoesQuadradoMagico():
    vetor = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    matrizes = permutations(vetor)
    matrizesValidas = []
    for i in list(matrizes):
        if (sum(i[0:3]) == sum(i[3:6]) == sum(i[6:9])):
            matrizesValidas.append(i)
    
    for i in list(matrizesValidas):
        print(i[0:3])
        print(i[3:6])
        print(i[6:9])
        print('')
    print(f'Total de combinações: {len(matrizesValidas)}')

combinacoesQuadradoMagico()
