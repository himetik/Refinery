lint:
	@flake8

install:
	@pip install -r requirements.txt
	@pip install -e .
	@python -m spacy download en_core_web_sm

uninstall:
	@pip uninstall -y refinery

reinstall:
	@pip uninstall -y refinery
	@pip install -e .

.PHONY: lint install uninstall reinstall
