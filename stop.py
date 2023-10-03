from src.utils import ler_celebridades, print_red, print_green, print_yellow, seguir, parar_de_seguir, print_gradient_banner
from instagram_private_api import Client
import time
import random
import os
from colorama import Fore, Back, Style, init
import json
def ler_tempos():
    with open("times.json", "r") as arquivo:
        dados = json.load(arquivo)
    return dados.get("long", 0), dados.get("fast", 0)
time1, time2 = ler_tempos()
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
            
        for index, username_to_unfollow in enumerate(celebridades):
            parar_de_seguir(api, username_to_unfollow, index)
            time.sleep(time2)
            if (index + 1) % 10 == 0:
                print_yellow('Aguardando...')
                time.sleep(time1)
                api = Client(username, password)
                    
    except Exception as e:
        print_red(f"Erro geral: {str(e)}")

if __name__ == "__main__":
    main()
