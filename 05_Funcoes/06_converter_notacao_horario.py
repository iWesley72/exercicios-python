def imprimirHora(horario):
    print(horario)

def converterFormatoHora(h, m):
    if (h >= 24 or h < 0 or m >=60 or m < 0):
        print('Desculpe, horário fornecido inválido!')
        return
    elif (h > 12):
        msg='P'
        hConvertido = h - 12
    else :
        msg = 'A'
        hConvertido = h
    novoHorario = str(hConvertido)+':'+str(m)+' '+msg+'M'
    imprimirHora(novoHorario)

while True:
    try:
        hora = int(input('\nHora: '))
        minuto = int(input('Minuto: '))
    except:
        print('Valor inválido! Digite novamente.')
        continue
    converterFormatoHora(hora, minuto)

