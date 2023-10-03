from src.utils import ler_celebridades, print_red, print_green, print_yellow, print_gradient_banner, comentar_postagem
from instagram_private_api import Client
import time
import random
import os
from colorama import Fore, Back, Style, init
init(autoreset=True)

def main():
    try:
        print_gradient_banner('./src/banner.txt')
        if os.path.exists("./login/login.txt"):
            with open("./login/login.txt", "r") as arquivo:
                lines = arquivo.readlines()
                username = lines[0].strip().split(": ")[1]
                password = lines[1].strip().split(": ")[1]
        else:
            username = input("Digite seu nome de usuário: ")
            password = input("Digite sua senha: ")
        api = Client(username, password)
        celebridades_file = './celebridades/celebridades.txt'
        celebridades = ler_celebridades(celebridades_file)
        random.shuffle(celebridades)

        comentario = input("Digite o texto que deseja comentar: ")

        while True:
            for index, username_to_comment in enumerate(celebridades):
                if comentar_postagem(api, username_to_comment, comentario):
                    print_green(f"Comentado no post de {username_to_comment}: {comentario}")
                else:
                    print_yellow(f"Nenhuma postagem encontrada para {username_to_comment}")

                time.sleep(3)

                if (index + 1) % 4 == 0:
                    print_yellow('Aguardando...')
                    time.sleep(30)
                    api = Client(username, password)

    except Exception as e:
        print_red(f"Erro geral: {str(e)}")

if __name__ == "__main__":
    main()