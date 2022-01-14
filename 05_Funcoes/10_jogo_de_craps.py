import random

def craps():
    n = random.randint(2, 12)
    if (n in [7, 11]):
        print(f'Você venceu! Tirou {n}.')
        return
    elif (n in [2, 3, 12]):
        print(f'Você perdeu! Tirou {n}.')
        return
    else:
        print(f'Você tirou {n}. Este é seu ponto. Deve tira-lo novamente para vencer. \nBoa sorte!')
        while True:
            j = random.randint(2, 12)
            if (j == 7):
                print('Você tirou 7 antes de tirar o ponto. Você perdeu!')
                return
            elif (j == n):
                print('Você tirou o ponto. Você venceu!\nParabéns!')
                return
            else:
                print(f'Você tirou {j}, ainda não tirou o ponto, vamos tentar denovo!')
                continue

craps()