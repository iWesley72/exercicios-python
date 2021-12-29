try:
    num1 = int(input('Digite o primeiro valor inteiro: '))
    num2 = int(input('Digite o segundo valor inteiro: '))
except:
    print('O valor digitado deve ser um número inteiro.')
    quit()
if (num1 > num2 and num1 - 1 != num2):
    soma = 0
    for i in range(num2+1, num1):
        soma += i
        print(i)
    print('O somatório dos inteiros é:', soma)
elif (num1 < num2 and num2 -1 != num1):
    soma = 0
    for i in range(num1+1, num2):
        soma += i
        print(i)
    print('O somatório dos inteiros é:', soma)
else:
    print('Por serem valores consecutivos não há inteiros entre eles.')