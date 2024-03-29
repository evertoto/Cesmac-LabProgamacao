import json
def salvarJson(dados, nome_arquivo):
    with open(nome_arquivo, 'w') as arquivo_json:
        json.dump(dados, arquivo_json, indent=4)

def carregarJson(nome_arquivo):
    try:
        with open(nome_arquivo, 'r') as arquivo_json:
            dados = json.load(arquivo_json)
    except FileNotFoundError:
        dados = []
    return dados
