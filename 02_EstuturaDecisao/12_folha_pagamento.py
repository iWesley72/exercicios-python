valorHora = float(input('Digite o valor da hora de trabalhado: R$ '))
horasTrabalhadas = float(input('Digite a quantidade de horas trabalhadas nesse mês: '))
salarioBruto = valorHora*horasTrabalhadas

if (salarioBruto <= 900):
    ir = 0
elif (salarioBruto <= 1500):
    ir = 0.05
elif (salarioBruto <= 2500):
    ir = 0.1
else:
    ir = 0.2

print('Salário bruto: R$', round(salarioBruto,2))
print('IR (' + str(ir*100) + '%): R$', round(salarioBruto*ir,2))
print('INSS (10%): R$', round(salarioBruto*0.1,2))
print('Sindicato (3%): R$', round(salarioBruto*0.03,2))
print('FGTS (11%): R$', round(salarioBruto*0.11,2))
totalDescontos = ir + 0.1 + 0.03
salarioLiquido = salarioBruto*(1-totalDescontos)
print('Total de descontos: R$', round(salarioBruto*totalDescontos,2))
print('Salário liquido: R$', round(salarioLiquido,2))
