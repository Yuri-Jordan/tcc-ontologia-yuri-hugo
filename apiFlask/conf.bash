docker stop apiflask
docker rm apiflask

docker build -t apiflask ./apiFlask
docker run --name apiflask -v $(pwd)/apiFlask:/app -d -p 5000:5000 apiflask
