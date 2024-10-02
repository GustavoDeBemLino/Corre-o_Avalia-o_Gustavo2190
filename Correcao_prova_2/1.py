LISTAS = []
cont = 0
dic = {}
for i in range(12):
    cont+=1
    lista = []
    dinheiro = float(input("Digite o quanto você ganhou neste mês:"))
    despesa = float(input("Digite qual a sua despesa neste mês"))
    lista.append(dinheiro)
    lista.append(despesa)
    dic.update({cont:lista})
    salario_liquido = list(map(lambda x,y: x-y, lista))
    LISTAS.append(salario_liquido)
print(salario_liquido)
sum_sal = sum(LISTAS)
print(sum_sal)
menor = list(filter(lambda x: x<0, LISTAS))
print(menor)
