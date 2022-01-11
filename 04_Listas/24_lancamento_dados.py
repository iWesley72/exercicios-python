import random

contador = [0]*6

for i in range(0, 100):
    valorDado = random.randint(1, 6)
    contador[valorDado-1] += 1
for i in range(1, 7):
    print(f'O valor {i} saiu {contador[i-1]} vezes')