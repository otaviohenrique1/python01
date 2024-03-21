# Exercicios
def verifica_se_numero_for_par_ou_impar():
  print("Verifica se o numero é par ou impar")
  numero = int(input("Digite um numero: "))
  if numero % 2 == 0:
    print("par")
  else:
    print("impar")

# verifica_se_numero_for_par_ou_impar()

def verifica_idade():
  print("Verifica idade")
  idade = int(input("Digite a idade: "))
  if 0 < idade <= 12:
    print("Criança")
  elif 13 < idade <= 18:
    print("Adolescente")
  elif idade > 18:
    print("Adulto")
  else:
    print("valor invalido")

# verifica_idade()

def verifica_usuario_e_senha():
  print("Verifica usuario e senha")
  usuario = "Alura"
  senha = "Alura123"
  usuario_digitado = input("Digite o usuario: ")
  senha_digitado = input("Digite a senha: ")
  if usuario == usuario_digitado and senha == senha_digitado:
    print("usuario e senha corretos")
  else:
    print("usuario ou senha incorretos")

# verifica_usuario_e_senha()

def quadrante():
  print("Quadrante")
  x = float(input("Digite a coordenada x: "))
  y = float(input("Digite a coordenada y: "))

  if x > 0 and y > 0:
    print("O ponto está no primeiro quadrante.")
  elif x < 0 and y > 0:
    print("O ponto está no segundo quadrante.")
  elif x < 0 and y < 0:
    print("O ponto está no terceiro quadrante.")
  elif x > 0 and y < 0:
    print("O ponto está no quarto quadrante.")
  else:
    print("O ponto está sobre um eixo ou na origem.")

quadrante()