#!/usr/bin/python3

import sys
arg = sys.argv

if len(arg) != 2:
    print("Usage: nqueens N")
    exit(1)

if not arg[1].isdigit():
    print("N must be a number")
    exit(1)

if int(arg[1]) < 4:
    print("N must be at least 4")
    exit(1)

n = int(arg[1])


def queens(n, i=0, a=[], b=[], c=[]):
    if i < n:
        for j in range(n):
            if j not in a and i + j not in b and i - j not in c:
                yield from queens(n, i + 1, a + [j], b + [i + j], c + [i - j])
    else:
        yield a


def solve(n):
    k = []
    i = 0
    for solution in queens(n, 0):
        for s in solution:
            k.append([i, s])
            i += 1
        print(k)
        k = []
        i = 0


solve(n)
