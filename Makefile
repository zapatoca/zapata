.PHONY: dependencies functional up destroy cleanup test coverage coverage-dependencies
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

dependencies: geckodriver-v0.28.0-$(OS).tar.gz cleanup
	mkdir geckodriver
	tar -xzf geckodriver-v0.28.0-$(OS).tar.gz -C geckodriver
	pip install --upgrade pip
	pip install -r tests/requirements.txt

cleanup:
	rm -rf geckodriver

functional: dependencies up
	pytest --driver=Firefox --driver-path=geckodriver/geckodriver tests/functional

test: functional
	make destroy cleanup

coverage-dependencies:
	pip install -r tests/unit/requirements.txt
	pip install -r zapata/reminders/requirements.txt

coverage: coverage-dependencies
	pytest --cov=zapata tests/unit
