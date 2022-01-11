salarios = []
abonos = []

print('Projeção de Gastos com Abono')
print('='*28)
print('')

while True:
    try:
        salario  = float(input('Salário: '))
    except:
        print('Salário inválid! Tente novamente.')
        continue
    if (salario == 0):
        break
    elif (salario <0):
        print('Salário inválido! Tente novamente.')
        continue
    else:
        salarios.append(salario)
        if (salario <= 500):
            abonos.append(100)
        else:
            abonos.append(salario*0.2)
        continue
print('')

print('{:<13} {:<13}'.format('Salário', 'Abono'))
for i in range(0, len(salarios)):
        print('{:<13} {:<13}'.format('R$ '+str(salarios[i]),'R$ '+str(round(abonos[i], 2))))

print(f'\nForam processados {len(salarios)} colaboradores')
print(f'Total gasto com abonos: R$ {round(sum(abonos), 2)}')
print(f'Valor mínimo pago a {abonos.count(100)} colaboradores')
print(f'Maior valor de abono pago: R$ {round(max(abonos), 2)}')