def cadastraProdutos(produtos):
    print("Tela de cadastro de produto")
    nomeproduto=str(input("Digite o nome do produto: "))
    precoproduto=int(input("Digite o seu preço: "))
    
    novoProduto = {
        'nome': nomeproduto,
        'preco': precoproduto,
    }

    produtos.append(novoProduto)

    print(novoProduto)

    return produtos