while true; do
    clear
    echo "Bem-vindo ao instabot!"
    echo "Escolha uma opção:"
    echo "1 - Ganhar seguidores."
    echo "2 - Ganhar seguidores 2."
    echo "3 - Comentar nas publicações das celebridades."
    echo "4 - Comentar automaticamente."
    echo "5 - Parar de seguir celebridades."
    echo "6 - Salvar suas informações de login."
    echo "7 - Remover suas informações de login."
    echo "8 - Sair."
    echo ""
    echo "Lembre-se: Alguns erros podem ocorrer durante a execução, como:"
    echo "Login incorreto - Verifique suas informações de login."
    echo "Bloqueio do Instagram - Acesse o Instagram e permita a entrada."
    echo "Queda na API - Pode ocorrer devido a problemas no Instagram."
    echo ""
    
    read choice

    case $choice in
        1)
            python3 main.py
            if [ $? -ne 0 ]; then
                echo -e "\e[31mErro no arquivo main.py\e[0m"
                echo "Pressione Enter para voltar ao menu..."
                read
            fi
            ;;
        2)
            python3 seguir.py
            if [ $? -ne 0 ]; then
                echo -e "\e[31mErro no arquivo seguir.py\e[0m"
                echo "Pressione Enter para voltar ao menu..."
                read
            fi
            ;;
        3)
            python3 comentar.py
            if [ $? -ne 0 ]; then
                echo -e "\e[31mErro no arquivo comentar.py\e[0m"
                echo "Pressione Enter para voltar ao menu..."
                read
            fi
            ;;
        4)
            python3 automatic.py
            if [ $? -ne 0 ]; then
                echo -e "\e[31mErro no arquivo automatic.py\e[0m"
                echo "Pressione Enter para voltar ao menu..."
                read
            fi
            ;;
        5)
            python3 stop.py
            if [ $? -ne 0 ]; then
                echo -e "\e[31mErro no arquivo stop.py\e[0m"
                echo "Pressione Enter para voltar ao menu..."
                read
            fi
            ;;
        6)
            python3 login.py
            error_code=$?
            if [ $error_code -eq 1 ]; then
                echo -e "\e[31mLogin incorreto\e[0m - Verifique suas informações de login."
            elif [ $error_code -eq 2 ]; then
                echo -e "\e[31mBloqueio do Instagram\e[0m - Acesse o Instagram e permita a entrada."
            elif [ $error_code -eq 3 ]; then
                echo -e "\e[31mQueda na API\e[0m - Pode ocorrer devido a problemas no Instagram."
            fi
            echo "Pressione Enter para voltar ao menu..."
            read
            ;;
        7)
            python3 logout.py
            if [ $? -ne 0 ]; then
                echo -e "\e[31mErro no arquivo logout.py\e[0m"
                echo "Pressione Enter para voltar ao menu..."
                read
            fi
            ;;
        8)
            echo "Saindo..."
            exit 0
            ;;
        *)
            echo "Opção inválida. Pressione Enter para tentar novamente."
            read
            ;;
    esac
done