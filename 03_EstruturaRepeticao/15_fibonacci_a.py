try:
    n = int(input('Digite até qual termo você deseja ver a séria de Fibonacci: '))
except:
    print('Valor inválido!')
    quit()
anterior = 1
penultimo = 1
print(penultimo, end=' ')
print(anterior, end=' ')
for n in range(3, n + 1):
    atual = anterior + penultimo
    penultimo = anterior
    anterior = atual
    print(atual, end=' ')