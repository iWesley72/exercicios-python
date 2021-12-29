# Para o campo nome
while True:
    nome = input('Digite seu nome: ')
    if (len(nome) > 3):
        break
    else:
        print('O campo nome deve ter mais de 3 caracteres!')
# Para o campo idade
while True:
    try:
        idade = int(input('Digite sua idade: '))
    except:
        print('O campo idade deve ser um número!')
    if (0<idade<150):
        break
    else:
        print('O campo idade deve ser um valor entre 0 e 150!')
# Para o campo salário
while True:
    try:
        salario = float(input('Digite seu salário: R$'))
    except:
        print('O campo salário deve ser um número!')
    if (salario > 0):
        break
    else:
        print('O campo salário deve ter um valor maior que 0!')
# Para o campo sexo
while True:
    sexo = input('Digite seu sexo(f/m): ')
    if (sexo.lower() == 'f' or sexo.lower() == 'm'):
        break
    else:
        print('O campo sexo deve ser preenchido com f-feminino ou m-masculino')
# Para o campo estado civil
while True:
    estadoCivil = input('Digite seu estado civil(S/C/D/V): ')
    if ('scdv'.find(estadoCivil.lower()) != -1):
        break
    else:
        print('O campo estado civil deve ser preenchido com s-solteiro, c-casado, d-divorciado ou v-viuvo.')