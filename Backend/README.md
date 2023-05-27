You need to install docker


cmd commands 

	docker network create foobar

	docker build . -t backend

	docker run --name backend --rm --network foobar -p 8000:8000 backend