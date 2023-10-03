from src.utils import seguir, parar_de_seguir, print_red, print_yellow, print_green, print_gradient_banner
from instagram_private_api import Client
import time
import os
from colorama import init

init(autoreset=True)

def main():
    try:
        print_gradient_banner('./src/banner.txt')
        
        while True:
            if os.path.exists("./login/login.txt"):
                with open("./login/login.txt", "r") as arquivo:
                    lines = arquivo.readlines()
                    username = lines[0].strip().split(": ")[1]
                    password = lines[1].strip().split(": ")[1]
            else:
                username = input("Digite seu nome de usuário: ")
                password = input("Digite sua senha: ")
            
            api = Client(username, password)
            celeb_username = input("Digite o username da celebridade: ")
            
            for _ in range(10):
                user_id = api.username_info(celeb_username)['user']['pk']
                followers = api.user_followers(user_id, rank_token=api.generate_uuid())
                
                for index, follower in enumerate(followers.get('users', [])):
                    if index >= 10:
                        break
                    
                    seguir(api, follower['username'], index)
                    time.sleep(5)
                
                print_yellow('Aguardando 120 segundos...')
                time.sleep(120)
            
            api = Client(username, password)
            for _ in range(10):
                user_id = api.username_info(celeb_username)['user']['pk']
                followers = api.user_followers(user_id, rank_token=api.generate_uuid())
                
                for index, follower in enumerate(followers.get('users', [])):
                    if index >= 10:
                        break
                    
                    seguir(api, follower['username'], index)
                    time.sleep(5)
                
                print_yellow('Aguardando 120 segundos...')
                time.sleep(120)
            
            print_yellow('Aguardando 120 segundos antes de parar de seguir...')
            time.sleep(120)
            
            api = Client(username, password)
            user_id = api.username_info(username)['user']['pk']
            following = api.user_following(user_id, rank_token=api.generate_uuid())
            
            for index, followed in enumerate(following.get('users', [])):
                if index >= 10:
                    break
                
                parar_de_seguir(api, followed['username'], index)
                time.sleep(3)
            
            print_yellow('Aguardando 120 segundos antes de parar de seguir os restantes...')
            time.sleep(120)
            
            api = Client(username, password)
            user_id = api.username_info(username)['user']['pk']
            following = api.user_following(user_id, rank_token=api.generate_uuid())
            
            for index, followed in enumerate(following.get('users', [])):
                if index >= 10:
                    break
                
                parar_de_seguir(api, followed['username'], index)
                time.sleep(3)
            
            print_yellow('Aguardando 100 segundos antes de recomeçar...')
            time.sleep(100)
            
    except Exception as e:
        print_red(f"Erro geral: {str(e)}")

if __name__ == "__main__":
    main()