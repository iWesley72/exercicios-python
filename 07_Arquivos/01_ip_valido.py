fHandle = open('entrada-ips.txt', 'r')
listaIP = list()
listaValido = list()
listaInvalido = list()
for linha in fHandle:
    listaIP.append(linha[:len(linha)-1])
fHandle.close()

for ip in listaIP:
    if (ip.count('.') == 3):
        valores = ip.split('.')
        teste = 0
        for valor in valores:
            valor = int(valor)
            if (1<=valor<=255):
                teste += 1
        if (teste == 4):
            listaValido.append(ip)
        else:
            listaInvalido.append(ip)
fHandle = open('saida-ips.txt', 'w')
fHandle.write(f'[Endereços válidos:]\n')
for i in listaValido: fHandle.writelines(f'{i}\n')
fHandle.write(f'[Endereços inválidos:]\n')
for i in listaInvalido: fHandle.writelines(f'{i}\n')
fHandle.close()