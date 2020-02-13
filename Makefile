clean:
	rm -rf *~ dist *.egg-info build target

build:
	maturin build

develop:
	maturin develop

test: develop
	python3 tests/test_decode.py
