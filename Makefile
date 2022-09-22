
run: build
	docker-compose up

build:
	docker build -t flask-app .
