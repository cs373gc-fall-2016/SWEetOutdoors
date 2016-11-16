#!/bin/bash
coverage run app/tests.py >  app/tests.tmp 2>&1
coverage report -m >> app/tests.out
cat app/tests.out
rm -f tests.tmp