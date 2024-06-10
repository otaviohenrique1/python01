import os

def exibir_nome_do_programa():
  print("""
      ░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
      ██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
      ╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
      ░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
      ██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
      ╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░
      """)

def exibir_opcoes():
  print('1. Cadastrar restaurante')
  print('2. Listar restaurante')
  print('3. Ativar restaurante')
  print('4. Sair\n')


def finalizar_app():
  os.system('cls')
  # os.system('clear') # no mac
  print('Finalizando o programa\n')

def opcao_invalida():
  print("Opção inválida\n")
  input('Digite uma tecla para voltar ao menu principal ')
  main()

def cadastrar_novo_restaurante():
  pass

def escolher_opcao():
  try:
    opcao_escolhida = int(input('Escolha uma opção\n'))
    # print(f'Você escolheu a opção {opcao_escolhida}')
    # print('Você escolheu a opção', opcao_escolhida)
    # print(opcao_escolhida == 1)
    # print(type(opcao_escolhida))
    # print(type(1))

    if opcao_escolhida == 1:
      # print('Cadastrar restaurante')
      cadastrar_novo_restaurante()
    elif opcao_escolhida == 2:
      print('Listar restaurantes')
    elif opcao_escolhida == 3:
      print('Ativar restaurantes')
    elif opcao_escolhida == 4:
      # print('Encerrando o programa')
      finalizar_app()
    else:
      opcao_invalida()
  except:
    opcao_invalida()

def main():
  os.system('cls')
  exibir_nome_do_programa()
  exibir_opcoes()
  escolher_opcao()

if __name__ == '__main__':
  main()