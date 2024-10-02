dic_pedido = {}
while True:
    pergunta = int(input("Escolha uma opção:\n1-Adicionar pedidos\n2-Atualizar pedido\n3-Remover pedido\n4-Filtrar pedidoss por cliente\n5-Visualizar todos pedidos\n6-Sair\n"))

    if pergunta == 1:
        lista = []
        nome = input("Digite o seu nome:")
        lista.append(nome)
        quant_pedido = int(input("Qual a quantidade de pedidos de você?"))
        for i in quant_pedido:
            pedido = input("Digite o seu pedido: ")
            lista.append(pedido)
        dic_pedido.update({nome:pedido})

    elif pergunta == 2:
        nome_da_troca = "Digite o nome do usúario que deseja trocar o pedido:"
        

    elif pergunta == 3:



    elif pergunta == 4:

    

    elif pergunta == 5:



    elif pergunta == 6:
        print("Fechando programa...")
        break