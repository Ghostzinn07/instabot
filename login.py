username = input("Digite o nome de usuário: ")
senha = input("Digite a senha: ")
with open("./login/login.txt", "w") as arquivo:
    arquivo.write(f"Nome de usuário: {username}\n")
    arquivo.write(f"Senha: {senha}\n")
print("As informações foram salvas.")