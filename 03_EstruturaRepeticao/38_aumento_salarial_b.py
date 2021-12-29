while True:
    try:
        salario = float(input('Salario atual: R$ '))
    except:
        print('Valor inválido! Tente novamente.')
        continue
    break

aumento = 0.015
for i in range(1, 2022-1996):
    salario *= (1+(aumento*i))
print(f'Salário em 2022: R$ {round(salario, 2)}')