num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
num3 = int(input('Digite o terceiro número: '))

if (num1>num2 and num2>num3):
    print(num1, 'é o maior e', num3, 'é o menor.')
elif (num1>num2 and num3>num2):
    print(num1, 'é o maior e', num2, 'é o menor.')
elif (num2>num1 and num1>num3):
    print(num2, 'é o maior e', num3, 'é o menor.')
elif (num2>num1 and num3>num1):
    print(num2, 'é o maior e', num1, 'é o menor.')
elif (num3>num1 and num1>num2):
    print(num3, 'é o maior e', num2, 'é o menor.')
else:
    print(num3, 'é o maior e', num1, 'é o menor.')