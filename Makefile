.PHONY: functional-dependencies coverage-dependencies dependencies up down \
	test functional coverage clean build sidecar
.EXPORT_ALL_VARIABLES:

UNAME := $(shell uname)

ifeq ($(UNAME), Linux)
	OS := linux64
endif
ifeq ($(UNAME), Darwin)
	OS := macos
endif

AWS_ACCESS_KEY_ID     := $(shell aws configure get aws_access_key_id)
AWS_SECRET_ACCESS_KEY := $(shell aws configure get aws_secret_access_key)
AWS_DEFAULT_REGION    := $(shell aws configure get region)

geckodriver-v0.28.0-$(OS).tar.gz:
	wget https://github.com/mozilla/geckodriver/releases/download/v0.28.0/geckodriver-v0.28.0-$(OS).tar.gz

dependencies:
	pip install --upgrade pip
	pip install -r tests/requirements.txt

coverage-dependencies:
	pip install -r tests/unit/requirements.txt
	pip install -r zapata/app/requirements.txt
	pip install -r zapata/reminders/requirements.txt

functional-dependencies: geckodriver-v0.28.0-$(OS).tar.gz
	mkdir geckodriver
	tar -xzf geckodriver-v0.28.0-$(OS).tar.gz -C geckodriver
	pip install -r tests/functional/requirements.txt
	pip install -r zapata/app/requirements.txt

coverage: dependencies coverage-dependencies
	python3 -m pytest --cov=zapata --cov-fail-under=50 --cov-report term-missing tests/unit

functional: dependencies functional-dependencies up
	python3 -m pytest --driver=Firefox --driver-path=geckodriver/geckodriver tests/functional

test: functional coverage

clean:
	rm -rf geckodriver
	docker-compose -f sidecar-compose.yml -f docker-compose.yml down --rmi all
	docker volume rm $$(docker volume ls -q)

down:
	docker-compose -f sidecar-compose.yml -f docker-compose.yml down

build:
	docker-compose -f sidecar-compose.yml -f docker-compose.yml build

sidecar: build
	docker-compose -f sidecar-compose.yml run --rm certbot

up: build sidecar
	export HOME=. && docker-compose up -d
	sleep 10
	docker-compose exec -T db psql -U zapata -d zapata -f /tmp/dump.sql
