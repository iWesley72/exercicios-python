horasTrabalhadas = float(input('Digite a quantidade de horas trabalhadas no mês: '))
valorHora = float(input('Digite o valor da hora trabalhada: '))
salarioBruto = horasTrabalhadas*valorHora
print('Salário bruto: R$', round(salarioBruto,2))
print('IR (11%): R$', round(salarioBruto*0.11, 2))
print('INSS (8%): R$', round(salarioBruto*0.08, 2))
print('Sindicato (5%): R$', round(salarioBruto*0.05, 2))
print('Salário líquido: R$', round((salarioBruto*(1-0.11-0.08-0.05)),2))