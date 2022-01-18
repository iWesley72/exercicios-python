print('Valida e corrige número de telefone')
telefone = list(input('Telefone: '))
if ('-' in telefone): telefone.remove('-')
if (len(telefone) == 7):
    print('Telefone possui 7 dígitos. Vou acrescentar o digito três na frente.')
    telefoneCorrigido = '3'+''.join(telefone)
    print(f'Telefone corrigo sem formatação: {telefoneCorrigido}')
    telefoneCorrigido = telefoneCorrigido[:4] + '-' + telefoneCorrigido[4:]
    print(f'Telefone corrigido com formatação: {telefoneCorrigido}')