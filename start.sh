    clear
    echo "Bem-vindo ao instabot!"
    echo "Escolha uma opção:"
    echo "1 - Ganhar seguidores."
    echo "2 - Comentar nas publicações das celebridades."
    echo "3 - Comentar automaticamente."
    echo "4 - Parar de seguir celebridades."
    echo "5 - Sair."

    read choice

    case $choice in
        1)
            python3 main.py
            ;;
        2)
            python3 comentar.py
            ;;
        3)
            python3 automatic.py
            ;;
        4)
            python3 stop.py
            ;;
        5)
            echo "Saindo..."
            exit 0
            ;;
        *)
            echo "Opção inválida. Pressione Enter para tentar novamente."
            read
            ;;
    esac
done