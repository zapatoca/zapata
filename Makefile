.PHONY: test-dependencies dependencies up down test functional unit clean \
	build
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
	pip install -r zapata/app/requirements.txt
	pip install -r zapata/reminders/requirements.txt

test-dependencies: geckodriver-v0.28.0-$(OS).tar.gz
	-mkdir geckodriver
	tar -xzf geckodriver-v0.28.0-$(OS).tar.gz -C geckodriver
	pip install -r tests/requirements.txt

unit: dependencies test-dependencies
	python3 -m pytest --cov=zapata --cov-fail-under=52 --cov-report term-missing tests/unit

functional: dependencies test-dependencies up
	python3 -m pytest --driver=Firefox --driver-path=geckodriver/geckodriver tests/functional

test: functional unit

clean:
	rm -rf geckodriver
	docker-compose down --rmi all
	docker volume rm $$(docker volume ls -q)

down:
	docker-compose down

build:
	docker-compose build

up: build
	export HOME=. && docker-compose up -d
	sleep 10
	docker-compose exec -T db psql -U zapata -d zapata -f /tmp/dump.sql
