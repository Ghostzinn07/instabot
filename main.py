from src.utils import ler_celebridades, print_red, print_green, print_yellow, seguir, parar_de_seguir, print_gradient_banner
from instagram_private_api import Client
import time
import random
import os
from colorama import Fore, Back, Style, init
init(autoreset=True)

def main():
    try:
        print_gradient_banner('./src/banner.txt')
        username = input("Digite seu nome de usuário: ")
        password = input("Digite sua senha: ")
        api = Client(username, password)        
        celebridades_file = './celebridades/celebridades.txt'
        celebridades = ler_celebridades(celebridades_file)
        random.shuffle(celebridades)
        
        while True:
            for index, username_to_follow in enumerate(celebridades):
                seguir(api, username_to_follow, index)
                time.sleep(10)
                if (index + 1) % 10 == 0:
                    print_yellow('Aguardando...')
                    time.sleep(70)
                    api = Client(username, password)     
            
            for index, username_to_unfollow in enumerate(celebridades):
                parar_de_seguir(api, username_to_unfollow, index)
                time.sleep(10)
                if (index + 1) % 10 == 0:
                    print_yellow('Aguardando...')
                    time.sleep(70)
                    api = Client(username, password)
                    
    except Exception as e:
        print_red(f"Erro geral: {str(e)}")

if __name__ == "__main__":
    main()