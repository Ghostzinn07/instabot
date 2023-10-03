import os
if os.path.exists("./login/login.txt"):

    with open("./login/login.txt", "w") as arquivo:
        arquivo.truncate(0)
    print("Informações de login foram limpas.")
else:
    print("Nenhuma informação de login encontrada para limpar.")