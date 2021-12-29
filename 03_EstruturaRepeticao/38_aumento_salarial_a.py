salario = 1000
aumento = 0.015
for i in range(1, 2022-1996):
    salario *= (1+(aumento*i))
print(f'Salário em 2022: R$ {round(salario, 2)}')