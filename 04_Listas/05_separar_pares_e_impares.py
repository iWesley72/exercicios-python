vetor = list()
par = list()
impar = list()
for i in range(0, 20):
    while True:
        try:
            num = int(input(f'Digite o {i+1}° número: '))
        except:
            print('Valor inválido! O número digitado deve ser um inteiro.')
            continue
        break
    if (num%2 == 0):
        par.append(num)
    else:
        impar.append(num)
    vetor.append(num)
print(f'Todos os números que você digitou: \n {vetor}')
print(f'Todos os números pares que você digitou: \n {par}')
print(f'Todos os números impares que você digitou: \n {impar}')