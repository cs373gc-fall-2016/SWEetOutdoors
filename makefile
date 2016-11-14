.DEFAULT_GOAL := test

# FILES :=                              \
#     Netflix.html                      \
#     Netflix.log                       \
#     Netflix.py                        \
#     RunNetflix.in                     \
#     RunNetflix.out                    \
#     RunNetflix.py                     \
#     TestNetflix.out                   \
#     TestNetflix.py                     

ifeq ($(CI), true)                # Travis CI
    PYTHON   := python
    PIP      := pip3.5
    PYLINT   := pylint
    COVERAGE := coverage-3.5
    PYDOC    := pydoc3
    AUTOPEP8 := autopep8
else                                   # UTCS
    PYTHON   := python
    PIP      := pip3.5
    PYLINT   := pylint3.5
    COVERAGE := coverage-3.5
    PYDOC    := pydoc3.4
    AUTOPEP8 := autopep8
endif

format:
	$(AUTOPEP8) -i app/tests.py 
	$(AUTOPEP8) -i app/__init__.py
	$(AUTOPEP8) -i application.py

IDB3.log:
	git log > IDB3.log

IDB3.html:
	./IDB3.sh

test: format
	./test.sh

clean:
	rm -f app/tests.out
	rm -f *.pyc app/*.pyc
	rm -f IDB3.html



# lint:
# 	find . -type f \( -name "*.py" -and -not -name "*_test.py" \) | xargs pylint -r n

# run:
# 	python sweapplication/application.py
