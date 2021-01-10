.PHONY: dependencies functional

UNAME := $(shell uname)

ifeq ($(UNAME), Linux)
	OS = linux64
endif
ifeq ($(UNAME), Darwin)
	OS = macos
endif

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
	pytest

test: functional
	make destroy cleanup
