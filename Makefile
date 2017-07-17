init: bloom.py
	pip install -r requirements.txt

bloom.py:
	(cd idiomatic; python -m tatsu bloom.tatsu -o bloom.py)

test: bloom.py
	py.test tests

clean:
	rm idiomatic/bloom.py

.PHONY: init test