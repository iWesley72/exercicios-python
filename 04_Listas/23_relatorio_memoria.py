# 1 megabyte = 1.048.576 bytes
handleUsuarios = open('usuarios.txt', 'r')
linhas = handleUsuarios.readlines()
funcionarios = []
espaco = []

for linha in linhas:
    funcionarios.append(linha[:15].strip())
    espaco.append(float(linha[15:].strip()))
handleUsuarios.close()

for i in range(0, len(espaco)):
    espaco[i] *= 1/1048576

handleRelatorio = open('relatorio.txt', 'w')
handleRelatorio.write('{:<24} {:<38} \n'.format('ACME Inc.', 'Uso do espaço em disco pelos usuários'))
handleRelatorio.write('-'*65 + '\n')
handleRelatorio.write('{:<5} {:<16} {:<20} {:<9}\n'.format('Nr.', 'Usuário', 'Espaço utilizado', '% uso'))
handleRelatorio.write('\n')

for i in range(0, len(funcionarios)):
    porcentagem = round(espaco[i]/sum(espaco)*100, 2)
    handleRelatorio.write('{:<5} {:<16} {:<20} {:<9}\n'.format(i+1, funcionarios[i], str(round(espaco[i], 2)) + ' MB', str(porcentagem) + '%'))

handleRelatorio.write(f'\nEspaço total ocupado: {round(sum(espaco), 2)} MB\n')
handleRelatorio.write(f'Espaço médio ocupado: {round(sum(espaco)/len(espaco), 2)} MB\n')
handleRelatorio.close()