import json

with open("dados.json") as arc:
    dados = json.load(arc)

cont = 0
cont2 = 0
soma_media = 0
maior = 0
menor = 0

for i in dados:
    if i['valor']!=0:

        if i['valor']>maior or maior==0:
            maior = i['valor']
        if i['valor']<menor or menor==0:
            menor = i['valor']

        soma_media += i['valor'] 
        cont += 1
for i in dados:
    if i['valor']>soma_media/cont:
        cont2 +=1

#print(maior, menor, soma_media, cont,soma_media/cont,cont2)
print("O maior valor de faturamento no mes foi: R$",maior,)
print("O menor valor de faturamento no mes foi: R$",menor)
print(cont2,"dia(s) no mes teve/tiveram o faturamento maior que a média")

