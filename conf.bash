#!/bin/bash
# Dá permissões à estas pastas pra o Servidor
chmod 777 -R apiLaravel/storage
chmod 777 -R apiLaravel/bootstrap/cache
# Roda o docker-compose que sobe os containers
docker-compose up -d
# Espera 5 segundos para que o servidor de banco possa inicializar
sleep 5
# Salva o id do container da api
idContainer=$(docker ps -aqf "name=apiLaravel")
# Instala as dependências do Laravel via Composer
docker exec --workdir /var/www/html $idContainer composer install
# Cria gera chave da aplicação
docker exec --workdir /var/www/html $idContainer php artisan key:generate
# Cria tabelas no banco
docker exec --workdir /var/www/html $idContainer php artisan migrate
# Popula valores padrão em algumas tabelas do banco
#sudo docker exec --workdir /var/www/html/api $idContainer php artisan db:seed
# Gera as chaves para autenticação OAuth2
#sudo docker exec --workdir /var/www/html/api $idContainer php artisan passport:install

/bin/bash apiFlask/conf.bash
