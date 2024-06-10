import os

restaurantes = [
    {"nome": "Praça", "categoria": "Japonesa", "ativo": False},
    {"nome": "Pizza Superma", "categoria": "Pizza", "ativo": True},
    {"nome": "Cantina", "categoria": "Italiano", "ativo": False},
]


def exibir_nome_do_programa():
    print(
        """
      ░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
      ██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
      ╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
      ░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
      ██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
      ╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░
      """
    )


def exibir_opcoes():
    print("1. Cadastrar restaurante")
    print("2. Listar restaurante")
    print("3. Ativar restaurante")
    print("4. Sair\n")


def exibir_subtitulo(texto):
    os.system("cls")
    # os.system('clear') # no mac
    print(texto)
    print()


def finalizar_app():
    exibir_subtitulo("Finalizando o programa\n")


def voltar_ao_menu_principal():
    input("\nDigite uma tecla para voltar ao menu principal")
    main()


def opcao_invalida():
    print("Opção inválida\n")
    voltar_ao_menu_principal()


def cadastrar_novo_restaurante():
    exibir_subtitulo("Cadastro de novos restaurantes\n")
    nome_do_restaurante = input("Digite o nome do restaurante que deseja cadastrar: ")
    categoria = input(
        f"Digite o nome da categoria do restaurante {nome_do_restaurante}: "
    )
    dados_do_restaurante = {
        "nome": nome_do_restaurante,
        "categoria": categoria,
        "ativo": False,
    }
    restaurantes.append(dados_do_restaurante)
    print(f"O restaurante {nome_do_restaurante} foi cadastrado com sucesso!")
    voltar_ao_menu_principal()


def listar_restaurantes():
    exibir_subtitulo("Listando os restaurantes\n")
    for restaurante in restaurantes:
        nome_restaurante = restaurante["nome"]
        categoria = restaurante["categoria"]
        ativo = restaurante["ativo"]
        print(f"- {nome_restaurante} | {categoria} | {ativo}")
    voltar_ao_menu_principal()


def escolher_opcao():
    try:
        opcao_escolhida = int(input("Escolha uma opção\n"))
        # print(f'Você escolheu a opção {opcao_escolhida}')
        # print('Você escolheu a opção', opcao_escolhida)
        # print(opcao_escolhida == 1)
        # print(type(opcao_escolhida))
        # print(type(1))

        if opcao_escolhida == 1:
            # print('Cadastrar restaurante')
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            # print('Listar restaurantes')
            listar_restaurantes()
        elif opcao_escolhida == 3:
            # print("Ativar restaurantes")
            alternar_estado_restaurante()
        elif opcao_escolhida == 4:
            # print('Encerrando o programa')
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()


def main():
    os.system("cls")
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()


if __name__ == "__main__":
    main()
