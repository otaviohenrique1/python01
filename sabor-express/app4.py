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

def escolher_opcao():
  opcao_escolhida = int(input('Escolha uma opção\n'))
  # print(f'Você escolheu a opção {opcao_escolhida}')
  # print('Você escolheu a opção', opcao_escolhida)
  # print(opcao_escolhida == 1)
  # print(type(opcao_escolhida))
  # print(type(1))

  if opcao_escolhida == 1:
    print('Cadastrar restaurante')
  elif opcao_escolhida == 2:
    print('Listar restaurantes')
  elif opcao_escolhida == 3:
    print('Ativar restaurantes')
  elif opcao_escolhida == 4:
    # print('Encerrando o programa')
    finalizar_app()
  else:
    print('Encerrando o programa')

def escolher_opcao2():
  opcao_escolhida = int(input('Escolha uma opção\n'))

  match opcao_escolhida:
    case 1:
      print('Adicionar restaurante')
    case 2:
      print('Listar restaurantes')
    case 3:
      print('Ativar restaurante')
    case 4:
      finalizar_app()
        # print('Finalizar app')
    case _:
      print('Opção inválida!')

def main():
  exibir_nome_do_programa()
  exibir_opcoes()
  escolher_opcao()

if __name__ == '__main__':
  main()