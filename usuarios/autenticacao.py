def autenticacao(cadastro): 
    print("Tela de login:")

    login = str(input("Digite seu e-mail de login: "))

    emails = [email['email'] for email in cadastro]

    try:
        index = emails.index(login)
    except:
        print("Usuario nao cadastrado")
        return

    senhaCorrespondente = cadastro[index]['senha']

    tentativaSenha = str(input("Digite sua senha: "))

    if tentativaSenha == senhaCorrespondente:
        print("Acesso liberado")
    else:
        print("Acesso negado")

    return tentativaSenha == senhaCorrespondente
