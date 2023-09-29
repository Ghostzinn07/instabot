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

python main.py