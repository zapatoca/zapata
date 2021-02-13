.PHONY: functional-dependencies functional up destroy cleanup test coverage coverage-dependencies dependencies
.EXPORT_ALL_VARIABLES:

UNAME := $(shell uname)

ifeq ($(UNAME), Linux)
	OS := linux64
endif
ifeq ($(UNAME), Darwin)
	OS := macos
endif

AWS_ACCESS_KEY_ID     := $(shell awscliv2 configure get aws_access_key_id)
AWS_SECRET_ACCESS_KEY := $(shell awscliv2 configure get aws_secret_access_key)
AWS_DEFAULT_REGION    := $(shell awscliv2 configure get region)

up:
ifeq ($(UNAME), Darwin)
	vagrant up dev
endif

destroy:
ifeq ($(UNAME), Darwin)
	vagrant destroy -f dev
endif

geckodriver-v0.28.0-$(OS).tar.gz:
	wget https://github.com/mozilla/geckodriver/releases/download/v0.28.0/geckodriver-v0.28.0-$(OS).tar.gz

dependencies:
	pip install --upgrade pip
	pip install -r tests/requirements.txt

coverage-dependencies:
	pip install -r tests/unit/requirements.txt
	pip install -r zapata/app/requirements.txt
	pip install -r zapata/reminders/requirements.txt

functional-dependencies: geckodriver-v0.28.0-$(OS).tar.gz cleanup
	mkdir geckodriver
	tar -xzf geckodriver-v0.28.0-$(OS).tar.gz -C geckodriver
	pip install -r tests/functional/requirements.txt
	pip install -r zapata/app/requirements.txt



coverage: dependencies coverage-dependencies
	python3 -m pytest --cov=zapata --cov-fail-under=50 --cov-report term-missing tests/unit

functional: dependencies functional-dependencies up
	python3 -m pytest --driver=Firefox --driver-path=geckodriver/geckodriver tests/functional

test: functional
	make destroy cleanup

cleanup:
	rm -rf geckodriver
