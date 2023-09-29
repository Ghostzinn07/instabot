from instagram_private_api import Client
import time
import random
from colorama import Fore, Back, Style, init
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
RESET = "\033[0m"

def ler_celebridades(filename):
    with open(filename, 'r') as file:
        celebridades = [line.strip() for line in file]
    return celebridades

def print_red(text):
    print(RED + text + RESET)

def print_green(text):
    print(GREEN + text + RESET)

def print_yellow(text):
    print(YELLOW + text + RESET)

def seguir(api, username_to_follow, index):
    try:
        user_info = api.username_info(username_to_follow)
        user_id = user_info['user']['pk']
        api.friendships_create(user_id)
        print_green(f'Seguindo {username_to_follow}')
    except Exception as e:
        print_red(f"Erro ao seguir {username_to_follow}: {str(e)}")

def parar_de_seguir(api, username_to_unfollow, index):
    try:
        user_info = api.username_info(username_to_unfollow)
        user_id = user_info['user']['pk']
        api.friendships_destroy(user_id)
        print_red(f'Parando de seguir {username_to_unfollow}')
    except Exception as e:
        print_red(f"Erro ao parar de seguir {username_to_unfollow}: {str(e)}")
        
def print_gradient_banner(filename):
    with open(filename, 'r') as banner_file:
        lines = banner_file.readlines()
        gradient_colors = [Fore.LIGHTMAGENTA_EX, Fore.LIGHTYELLOW_EX]

        for line in lines:
            for color in gradient_colors:
                print(color + line.strip())
                time.sleep(0.05)
