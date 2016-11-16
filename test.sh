#!/bin/bash
coverage run tests.py >  tests.tmp 2>&1
coverage report -m >> tests.out
cat tests.out
rm -f tests.tmp