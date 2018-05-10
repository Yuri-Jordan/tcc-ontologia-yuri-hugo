docker stop apiFlask
docker rm apiFlask

docker run --name apiFlask --restart=always \
	-p 8000:80 \
	-v $(pwd)/apiFlask:/app \
	-d jazzdd/alpine-flask

docker exec --workdir /usr/lib/python2.7 apiFlask pip install twitter
