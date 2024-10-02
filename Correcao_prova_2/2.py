cont = 0
dic = {}

def Cadastro():
    nome = input("Digite o nome do funcionário:")
    salario = int(input("Digite o quanto o seu funcionário ganha: "))
    dic.update({nome:salario})


while True:
    pergunta = int("Digite o que desejás fazer:\n1-Cadastrar funcionario\n2-Mostrar funcionários específicos\n3-Aumento de funcionário\n4-Média salarial dos funcionários\n5-Funcionário com o maior e o menor salário\n6-Sair\n")

    if pergunta == 1:
        print(Cadastro())

    elif pergunta == 2:
        v_usuario = int(input("Digite um valor que mostrará certos funcionários que tem o salário maior que esse valor: "))
        for i in dic.values():
            valor_acima = filter(lambda x,y: x>y , v_usuario, i)
            print(valor_acima)

    elif pergunta == 3:
        porcentagem_aumento = map(lambda x: x*0.15,valor_acima)
        aumento = dict(map(lambda x,y: x+y,porcentagem_aumento,valor_acima  ))
        print(aumento)

    elif pergunta == 4:
        for a in dic.values():
            cont+=1
        sum_med = sum(dic.values())
        media = sum_med/cont
        print(media)

    elif pergunta == 5:
        max_fun = max(dic.values())
        print(max_fun)

        min_fun = min(dic.values())
        print(min_fun)

    elif pergunta == 6:
        print("Fechando o programa...")
        break

