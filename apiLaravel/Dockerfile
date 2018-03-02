FROM php:7.1-apache

# Instala PHP e extenxsões
RUN apt-get update && apt-get install -y \
  libpq-dev \
  && rm -r /var/lib/apt/lists/* \
  && docker-php-ext-install \
  pdo_pgsql \
  zip \
  opcache

# Instala composer
RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/bin --filename=composer

# Envia arquivo de configuração do apache para dentro do container
COPY apache2-laravel.conf /etc/apache2/sites-available/laravel.conf
RUN a2dissite 000-default.conf && a2ensite laravel.conf && a2enmod rewrite

RUN usermod -u 1000 www-data && groupmod -g 1000 www-data

WORKDIR /var/www/html
