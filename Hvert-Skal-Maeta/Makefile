all: style-check type-check unittest test
	@echo "All done..."

unittest:
	pytest -v hsm_test.py
	
test:
	@cat 1.in | python hsm.py | diff - 1.ans
	@cat 2.in | python hsm.py | diff - 2.ans
	@echo "All local test passed..."

style-check:
	flake8 .

type-check:
	mypy --strict .

kattis:
	@kattis -f hsm.py
	