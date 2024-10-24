def adicionar_contato(contatos, novo_contato):
    contato = {
      "nome": novo_contato["nome"],
      "telefone": novo_contato["telefone"],
      "email": novo_contato["email"],
      "favorito": True if novo_contato["favorito"] else False
    }
    contatos.append(contato)
    print(f"\nContato {novo_contato['nome']} adicionado com sucesso")
    return None


def visualizar_contatos(contatos):
    print("\n Lista de Contatos: ")
    if len(contatos) > 0:
        for index, item in enumerate(contatos, start=1):
            favorito = "☆" if item["favorito"] else ""
            nome = item["nome"]
            fone = item["telefone"]
            email = item["email"]
            print(
                f"\n{index}. {nome} - "
                f"Telefone: {fone} - Email: {email} {favorito}"
              )
    else:
        print("Nenhum contato adicionado à agenda.")
    return None


def editar_contato(contatos, indice, nome, telefone, email):
    indice_ajustado = int(indice) - 1
    if (indice_ajustado >= 0 and indice_ajustado < len(contatos)):
        if contatos[indice_ajustado]:
            if (nome):
                contatos[indice_ajustado]["nome"] = nome
            if (telefone):
                contatos[indice_ajustado]["telefone"] = telefone
            if (email):
                contatos[indice_ajustado]["email"] = email
            print(
                f"Contato {indice} atualizado com sucesso!"
                if nome or email or telefone else "")
        else:
            print("Contato inexistente!")
    return None


def marcar_ou_desmarcar_favorito(contatos, indice, favorito):
    indice_ajustado = int(indice) - 1
    contato_favorito = True if favorito == "S" else False

    if (indice_ajustado >= 0 and indice_ajustado < len(contatos)):
        if (contatos[indice_ajustado]):
            contatos[indice_ajustado]["favorito"] = contato_favorito
            msg_favorito = f"Contato {indice} foi marcado como favorito"
            msg_desf = f"Contato {indice} foi desmarcado como favorito"
            mensagem = msg_favorito if contato_favorito else msg_desf
            print(f"{mensagem}")

    return None


def mostrar_favoritos(contatos, favoritos):
    if len(contatos) > 0:
        for contato in contatos:
            if contato["favorito"]:
                favoritos.append(contato)
        if len(favoritos) > 0:
            print("Lista de favoritos: ")
        for indice, contato in enumerate(favoritos, start=1):
            print(f"{indice}. {contato['nome']} - "
                  f"Telefone: {contato['telefone']} - "
                  f"Email: {contato['email']}"
                  )
    return None


def apagar_contato(contatos, indice):
    indice_ajustado = int(indice) - 1
    if indice_ajustado >= 0 and indice_ajustado < len(contatos):
        contato = contatos[indice_ajustado]
        if contato:

            contatos.remove(contato)
            print(f"Contato {indice} apagado com sucesso")
        else:
            print(f"O contato com código {indice} não existe")
    else:
        print(f"Código {indice} inexistente!")
    return None
