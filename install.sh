clear 
     echo "Verificando atualizações..." 
  
     if ! pip3 show instagram_private_api &> /dev/null; then 
         echo "Instalando a dependência 'instagram_private_api'..." 
         pip3 install instagram_private_api 
     else 
         echo "A API do Instagram está atualizada." 
     fi  
     if ! pip3 show instagram_private_api &> /dev/null; then 
         echo "Instalando a dependência 'instaloader'..." 
         pip3 install instagram_private_api 
     else 
         echo "A biblioteca instaloader está atualizada." 
     fi 
     if ! pip3 show colorama &> /dev/null; then 
         echo "Instalando a dependência 'colorama'..." 
         pip3 install colorama 
     else 
         echo "Todas as bibliotecas estão atualizadas." 
     fi 
sh start.sh