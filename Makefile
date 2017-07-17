init:
	pip install -r requirements.txt
	python -m tatsu bloom.tatsu -o bloom.py

test:
	py.test tests

.PHONY: init test