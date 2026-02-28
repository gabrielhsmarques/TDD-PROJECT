run:
	@uvicorn store.main:app --reload

install:
	pip install -r requirements.txt
	pre-commit install

test:
	@pytest
