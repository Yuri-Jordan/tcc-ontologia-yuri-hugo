FROM alpine

# instala Flask
RUN apk add --no-cache bash git nginx uwsgi uwsgi-python py2-pip \
	&& pip2 install --upgrade pip \
	&& pip2 install flask


# compia arquivos de configuração para dentro do container
COPY nginx.conf /etc/nginx/nginx.conf
