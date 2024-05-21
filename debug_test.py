# -*- coding: utf-8 -*-
"""
Warning! This code has deliberate errors
if you run without a breakpoint
you will get an endless loop, which will cause problems
for the sake of your sanity, run this code in debug mode only
"""


## a normally-executing while loop
"""
 i = 0
 j = 0
 while i <= 10:
    i += 1
    print("Hi there")
"""

## a bad while loop
"""
i = 0
j = 0
while i > 10:
    i += 1
    print("Hi there")
"""

## another bad while loop
"""
i = 10
j = 0
while i < 10:
     i += 1
     print("Hi there")
"""

## and another one
"""
i = 0
j = 0
while i <= 10:
    j += 1
    print("Hi there")
"""
## how many ways can we mess this up?
"""
i = 0
j = 0
while i <= 10:
    i -= 1
    print("Hi there")
"""