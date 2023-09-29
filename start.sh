if ! pip show instagram_private_api &> /dev/null; then
    echo "Instalando a dependência 'instagram_private_api'..."
    pip install instagram_private_api
else
    echo "Verificando as dependências..."
fi

if ! pip show colorama &> /dev/null; then
    echo "Instalando a dependência 'colorama'..."
    pip install colorama
else
    echo "Verificando as dependências..."
fi

echo "Escolha uma opção:"
echo "1 - Ganhar seguidores."
echo "2 - Parar de seguir celebridades."

read choice

if [ $choice -eq 1 ]; then
    python main.py
elif [ $choice -eq 2 ]; then
    python stop.py
else
    echo "Opção inválida."
fi