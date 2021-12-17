salarioAntes = float(input('Informe o seu salário: R$ '))

if (salarioAntes <= 280):
    ajuste = 0.2
elif (salarioAntes <= 700):
    ajuste = 0.15
elif (salarioAntes <= 1500):
    ajuste = 0.1
else:
    ajuste = 0.05

print('Salário antes: R$', salarioAntes)
print('Percentual aplicado:', ajuste*100, '%.')
print('Valor do aumento: R$', round(salarioAntes*ajuste,2))
print('Novo salário: R$', round(salarioAntes*(1+ajuste),2))