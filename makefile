format:
	find . -type f \( -name "*.py" \) | xargs autopep8 -i

lint:
	find . -type f \( -name "*.py" -and -not -name "*_test.py" \) | xargs pylint -r n

run:
	python sweapplication/application.py