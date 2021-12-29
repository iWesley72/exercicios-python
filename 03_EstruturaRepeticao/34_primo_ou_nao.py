while True:
    try:
        n = int(input('Digite o valor a ser testado: '))
    except:
        print('Valor inválido! Digite novamente.')
        continue
    if (n <= 1):
        print('O valor digitado deve ser um inteiro positivo maior que 1.')
        continue
    else:
        break
teste = True
for i in range(2, n):
    if (n%i == 0):
        teste = False
        break
    else:
        continue
if (teste == False):
    print(f'{n} não é um número primo!')
else:
    print(f'{n} é um número primo!')