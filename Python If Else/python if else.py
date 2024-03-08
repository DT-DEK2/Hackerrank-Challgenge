#!/bin/python3
# https://www.hackerrank.com/challenges/py-if-else/problem?isFullScreen=true
import math
import os
import random
import re
import sys

def check_weird(n):
    if n % 2 != 0 or (n % 2 == 0 and n in range(6, 21)):
        return 'Weird'
    elif n % 2 == 0 and (n in range(2, 6) or n > 20):
        return 'Not Weird'

if __name__ == '__main__':
    n = int(input().strip())
    print(check_weird(n))
