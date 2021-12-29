penultimo = 1
anterior = 1
print(penultimo, end=' ')
print(anterior, end=' ')
atual = penultimo + anterior
print(atual, end=' ')
while True:
    penultimo = anterior
    anterior = atual
    atual = penultimo + anterior
    print(atual, end=' ')
    if (atual > 500):
        break