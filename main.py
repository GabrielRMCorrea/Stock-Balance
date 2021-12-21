from yahoo_fin import stock_info as si
import json

with open('Papeis.json', encoding='utf8') as x:
    jsonfile = json.load(x)

TotalInvestido = 0.00
TotalInvista = 0.00

print('Você tem: ')
for i in jsonfile['Papeis']:
    try:
        i['Preco'] = float(si.get_live_price(i['Cod']))
    except ValueError:
        raise Exception(f"{i['Cod']} sem preço")
    tempval = int(i['Quantidade']) * float(i['Preco'])
    print(f"R${tempval:.2f} de {i['Cod']}")
    TotalInvestido += tempval

print(f'E o total investido é R${TotalInvestido:.2f}')

with open('Papeis.json', 'w', encoding='utf8')  as y:
    try:
        json.dump(jsonfile,y,indent= 2, ensure_ascii=True)
    except:
        raise Exception("erro ao escrever no arquivo")
ValpIvest = float(input('Quanto você tem para investir?'))

for i in jsonfile['Papeis']:
    invistaqtd = round(((TotalInvestido + ValpIvest) / len(jsonfile['Papeis']) - (int(i['Quantidade']) * float(i['Preco']))) / float(i['Preco']) )
    TotalInvista = TotalInvista + (invistaqtd * float(i['Preco']))
    print(f"compre {invistaqtd}x {i['Cod']} por: R${i['Preco']:.2f} cada, totalizando {invistaqtd * float(i['Preco']):.2f}")

print(f'Investindo um total de R${TotalInvista:.2f}')


