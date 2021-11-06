#!/usr/bin/env python3

from itertools import count

x=count(1)

for _ in range(10):
    print(next(x))