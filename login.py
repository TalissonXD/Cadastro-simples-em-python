#Sistema de login simples
class Usuario:
  def __init__(self, nome, senha):
    self.nome = nome
    self.senha = senha
  def mostrar_infor(self, nome):
    senha = input("Digite a senha: ")
    if nome == self.nome and senha == self.senha:
      print("Acesso aceito")
      print("INFORMAÇÕES DE LOGIN")
      print(f"O usuario se chama {self.nome}")
      print(f"Sua senha é {senha}")
    else:
      print("Acesso negado")
      print("Nome de usuario ou senha incorretos")
def main():
  usuarios = {}
  while True:
    print("SISTEMA DE CADASTRO E LOGIN")
    opcoes = ["1","2","3","4", "5"]
    print("1 - Cadastrar usuario")
    print("2 - Fazer login")
    print("3 - Mostrar informações de cadastro")
    print("4 - Mostrar todos usuarios")
    print("5 - Sair")
    opcao = input("Que ação deseja fazer? ")
    while opcao not in opcoes:
      print("Opção Invalida")
      print("1 - Cadastrar usuario")
      print("2 - Fazer login")
      print("3 - Mostrar informações de cadastro")
      print("4 - Sair")
      opcao = input("Que ação deseja fazer? ")
    if opcao == "1":
      nome = input("Escolha seu nome de usuario").upper()
      senha = input("Crie sua senha(Minimo de caracteres: 8)")
      while len(senha) < 8:
        print("Poucos caracteres")
        senha = input("Crie sua senha(Minimo de caracteres: 8)")
      usuarios[nome] = Usuario(nome, senha)
      print("Usuario Cadastrado")
      print("-"*80)
    elif opcao == "2":
      if usuarios == {}:
        print("Nenhum usuario cadastrado")
        print("-"*80)
      else:
        usuario = input("Digite seu nome de usuario: ").upper()
        senhalogin = input("Digite a senha: ")
        if usuario in usuarios and senhalogin == usuarios[usuario].senha:
          print("Login Feito")
        else:
          print("Informações invalidas")
          print("-"*80)
    elif opcao == "3":
      if usuarios == {}:
        print("Nenhum usuario cadastrado")
      else:
        nome = input("Digite o nome do seu Usuario: ").upper()
        usuarios[nome].mostrar_infor(nome)
      print("-"*80)
    elif opcao == "4":
      if usuarios == {}:
        print("nenhum usuario cadastrado")
        print("-"*80)
        
      for user in usuarios.values():
        print(user.nome)
        print("-"*80)
    else:
      break
main()
      
    
  
    
    
  

