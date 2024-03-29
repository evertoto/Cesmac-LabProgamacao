from usuarios.cadastro import cadastraUsuario
from usuarios.autenticacao import autenticacao
from produtos.cadastraProdutos import cadastraProdutos
from produtos.listagem import listaProdutos
from filesystem import *

cadastroPath = "data/cadastro.json"
produtosPath = "data/produtos.json"

cadastro = carregarJson(cadastroPath)

autenticado = False

opcao = int(input("Quer fazer login ou se cadastrar?\n1-Cadastrar\n2-Login\n")) == 1

if opcao:
    cadastraUsuario(cadastro)
else:
    autenticado = autenticacao(cadastro)

salvarJson(cadastro, cadastroPath)

if not autenticado:
    quit()

produtos = carregarJson(produtosPath)

opcao = int(input("Quer cadastrar ou listar produtos?\n1-Cadastrar\n2-Listar\n")) == 1

if opcao:
    produtos = cadastraProdutos(produtos)
    salvarJson(produtos, produtosPath)
else:
    listaProdutos(produtos)




