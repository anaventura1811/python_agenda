import functions as fn


contatos = []
favoritos = []

while True:
    print("\nMenu da agenda de contatos:")
    print("1. Adicionar novo contato")
    print("2. Visualizar lista de contatos")
    print("3. Editar contato")
    print("4. Marcar ou desmarcar contato como favorito")
    print("5. Mostrar lista de contatos favoritos")
    print("6. Apagar contato")
    print("7. Sair da agenda")

    escolha = input("Digite a sua escolha: ")

    if escolha == "1":
        nome_contato = input(
            "Escreva o nome do contato que deseja adicionar à sua agenda: "
        )
        email_contato = input("Escreva o email do contato: ")
        telefone_contato = input("Escreva o telefone do contato: ")
        favorito_contato = input(
            "Deseja marcar este contato como favorito?"
            "\nDigite S para Sim e N para Não: \n"
        )
        novo_contato = {
            "nome": nome_contato,
            "telefone": telefone_contato,
            "email": email_contato,
            "favorito": True if favorito_contato == "S" else False
        }
        fn.adicionar_contato(contatos, novo_contato=novo_contato)

    elif escolha == "2":
        fn.visualizar_contatos(contatos)

    elif escolha == "3":
        indice = input("Escreva o código do contato: ")
        print(
            "Altere os campos que queira editar.\n"
            "Caso não deseje editar um dos campos, apenas deixe em branco e\n"
            "pressione 'Enter' para continuar"
          )
        nome = input("Nome do contato: ")
        telefone = input("Telefone do contato: ")
        email = input("Email do contato: ")
        fn.editar_contato(
            contatos,
            indice=indice,
            nome=nome,
            telefone=telefone,
            email=email
          )
        fn.visualizar_contatos(contatos)

    elif escolha == "4":
        fn.visualizar_contatos(contatos)
        indice = input("Digite o código do contato que "
                       "deseja marcar ou desmarcar como favorito: ")
        favoritar_ou_desfavoritar = input(
            "Deseja marcar ou desmarcar o contato como favorito?\n"
            "Para marcar como favorito, digite S\n"
            "Para desmarcar, digite qualquer tecla\n"
            )
        fn.marcar_ou_desmarcar_favorito(
            contatos=contatos,
            indice=indice,
            favorito=favoritar_ou_desfavoritar
          )
        fn.visualizar_contatos(contatos)

    elif escolha == "5":
        fn.mostrar_favoritos(contatos, favoritos)

    elif escolha == "6":
        fn.visualizar_contatos(contatos)
        contato = input("Digite o código do contato que deseja apagar: ")
        fn.apagar_contato(contatos=contatos, indice=contato)

    elif escolha == "7":
        break

print("Programa finalizado")
