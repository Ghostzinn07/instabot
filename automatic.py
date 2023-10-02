from src.utils import ler_celebridades, print_red, print_green, print_yellow, print_gradient_banner
import instaloader
from instagram_private_api import Client
import time
import random
import os
from colorama import Fore, Back, Style, init

loader = instaloader.Instaloader()
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
        total_postagens_anterior = 0

        while True:
            profile = instaloader.Profile.from_username(loader.context, perfil_alvo)
            num_publicacoes = profile.mediacount
            if num_publicacoes > total_postagens_anterior:
                total_postagens_anterior = num_publicacoes
                user_info = api.username_info(perfil_alvo)
                user_id = user_info['user']['pk']
                if user_id:
                    num_posts = user_info['user']['media_count']
                    num_posts_to_check = min(5, num_posts)

                    if num_posts_to_check > 0:
                        user_feed = api.user_feed(user_id)
                        recent_posts = user_feed.get("items", [])[:num_posts_to_check]

                        if recent_posts:
                            recent_posts.sort(key=lambda x: x['taken_at'], reverse=True)
                            latest_post = recent_posts[0]

                            media_id = latest_post['id']

                            if media_id not in postagens_comentadas:
                                comentarios = [comentario1, comentario2, comentario3]
                                comentario_escolhido = random.choice(comentarios)

                                if api.post_comment(media_id, comentario_escolhido):
                                    print_green(f"Comentado no post mais recente de {perfil_alvo}: {comentario_escolhido}")
                                    postagens_comentadas.append(media_id)
                                    time.sleep(3)
                                else:
                                    print_yellow(f"Não foi possível comentar no post de {perfil_alvo}")

                    time.sleep(10)
                else:
                    print_red(f"Usuário {perfil_alvo} não encontrado")

    except Exception as e:
        print_red(f"Erro geral: {str(e)}")

if __name__ == "__main__":
    main()