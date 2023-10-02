while true; do
    clear
    echo "Bem-vindo ao instabot!"
    echo "Use o comando: sh install.sh para baixar as dependências."
    sleep(2)
    echo "Escolha uma opção:"
    echo "1 - Ganhar seguidores."
    echo "2 - Comentar nas publicações das celebridades."
    echo "3 - Parar de seguir celebridades."
    echo "4 - Sair."

    read choice

    case $choice in
        1)
            python3 main.py
            ;;
        2)
            python3 comentar.py
            ;;
        3)
            python3 stop.py
            ;;
        4)
            echo "Saindo..."
            exit 0
            ;;
        *)
            echo "Opção inválida. Pressione Enter para tentar novamente."
            read
            ;;
    esac
done