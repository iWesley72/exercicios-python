grupos = [0]*9

for i in range(0, 5):
    while True:
        try:
            vendasBrutas = float(input('Vendas brutas: R$ '))
        except:
            print('Valor inválido! Digite novamente.')
            continue
        break
    grupo = (200 + 0.09*vendasBrutas)/1000
    if (0.2<=grupo<=0.299): grupos[0]+=1
    elif (0.3<=grupo<=0.399): grupos[1]+=1
    elif (0.4<=grupo<=0.499): grupos[2]+=1
    elif (0.5<=grupo<=0.599): grupos[3]+=1
    elif (0.6<=grupo<=0.699): grupos[4]+=1
    elif (0.7<=grupo<=0.799): grupos[5]+=1
    elif (0.8<=grupo<=0.899): grupos[6]+=1
    elif (0.9<=grupo<=0.999): grupos[7]+=1
    elif (1<=grupo): grupos[8]+=1

print('{:<8} {:<8} {:<8} {:<8} {:<8} {:<8} {:<8} {:<8} {:<8}'.format('200-299', '300-399', '400-499', '500-599', '600-699', '700-799', '800-899', '900-999', '1000-')
)
print('{:<8} {:<8} {:<8} {:<8} {:<8} {:<8} {:<8} {:<8} {:<8}'.format(grupos[0],grupos[1],grupos[2],grupos[3],grupos[4],grupos[5],grupos[6],grupos[7],grupos[8],))