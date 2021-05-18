# Arithmetic Functions
from math import *


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def mul(n1, n2):
    return n1 * n2


def div(n1, n2):
    if n2 == 0:
        return 'inf'

    return n1 / n2


def fact(n):
    if n == 0:
        return 1

    return n * fact(n - 1)


def mod(n1, n2):
    if n1 == 0 and n2 == 0:
        return 0
    elif n1 != 0 and n2 == 0:
        return n1
    return n1 % n2


def sqrt(n):
    if n < 0:
        return 'null'
    return sqrt(n)


