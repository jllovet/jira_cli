setup:
	# Create python virtualenv & source it
	# Run this source command after running `make setup`
	# source .venv/bin/activate
	python3 -m venv .venv

environment:
	cp .private.env .env

install:
	pip3 install -r requirements.txt --require-virtualenv

clean:
	find . | grep -E "(__pycache__|\.pyc|\.pyo$\)" | xargs rm -rf
