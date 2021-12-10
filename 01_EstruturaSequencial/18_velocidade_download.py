tamanhoArquivo = float(input('Digite o tamanho do arquivo em MB: '))
velocidade = float(input('Digite a velocidade da sua internet em Mbps: '))
vFinal = velocidade*0.125*60
print('O download demorará', round(tamanhoArquivo/vFinal), 'minutos.')