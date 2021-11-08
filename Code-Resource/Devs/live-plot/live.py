#!/usr/bin/env python3

# Guide for live plot
# https://github.com/CoreyMSchafer/code_snippets/blob/master/Python/Matplotlib/09-LiveData/starting_code.py

from itertools import count

x=count(1)

for _ in range(10):
    print(next(x))