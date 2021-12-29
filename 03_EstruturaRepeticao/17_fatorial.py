try:
    n = int(input('Digite o valor que você deseja saber o fatorial: '))
except:
    print('Valor inválido!')
    quit()
if (n <= 0):
    print('O valor deve ser um inteiro positivo não nulo!')
    quit()
fatorial = 1
for i in range(1, n + 1):
    fatorial *= i
print(f'Fatorial de {n} é {fatorial}.')