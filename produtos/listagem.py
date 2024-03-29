def listaProdutos(produtos): 
    print("Tela de Visualização de Produtos")
    
    for produto in produtos:
        print("Nome: ", produto["nome"])
        print("Preco: ", produto["preco"],"\n")