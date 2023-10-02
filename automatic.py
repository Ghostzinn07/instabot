from src.utils import ler_celebridades, print_red, print_green, print_yellow, print_gradient_banner
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

        perfil_alvo = input("Digite o nome do perfil que deseja comentar: ")
        comentario1 = input("Digite a primeira mensagem que deseja comentar: ")
        comentario2 = input("Digite a segunda mensagem que deseja comentar: ")
        comentario3 = input("Digite a terceira mensagem que deseja comentar: ")

       
        postagens_comentadas = []

        while True:
            user_info = api.username_info(perfil_alvo)
            user_id = user_info['user']['pk']

            if user_id:

                timeline = api.user_feed(user_id)
                latest_post = timeline.get("items", [])[0]

                if latest_post:
                    media_id = latest_post['id']

                   
                    if media_id not in postagens_comentadas:
                        comentarios = [comentario1, comentario2, comentario3]
                        comentario_escolhido = random.choice(comentarios)

                        if api.post_comment(media_id, comentario_escolhido):
                            print_green(f"Comentado no post de {perfil_alvo}: {comentario_escolhido}")
                            postagens_comentadas.append(media_id)
                        else:
                            print_yellow(f"Não foi possível comentar no post de {perfil_alvo}")

                
                time.sleep(60)

            else:
                print_red(f"Usuário {perfil_alvo} não encontrado")

    except Exception as e:
        print_red(f"Erro geral: {str(e)}")

if __name__ == "__main__":
    main()