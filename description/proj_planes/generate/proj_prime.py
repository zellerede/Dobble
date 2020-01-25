#!/usr/bin/env python

""" Generates lines on affine plane based on a NearField of 9 elements
    and writes it in a json file """

import json

N = 11  # any odd prime

def init_vars(n=N):
    global N, Nhalf, R, Field
    N = n
    Nhalf = N // 2
    R = tuple(range(-Nhalf, Nhalf+1))
    GFp.elements = {}
    GFp.range = list(map(GFp, R))
    Field = GFp

def modN(num):
    return (num + Nhalf) % N - Nhalf

class GFp:
    elements = {}

    def __new__(cls, num):
        num = modN(num)
        elem = cls.elements.get(num)
        if elem is not None: return elem
        elem = object.__new__(cls)
        cls.elements[num] = elem
        return elem

    def __init__(self, num):
        num = modN(num)
        self.num = num
        self.id = num + Nhalf
    
    def __repr__(self):
        return repr(self.num)

    def __mul__(self, other):
        return type(self)(self.num * other.num)

    def __add__(self, other):
        return type(self)(self.num + other.num)

def generateAllLines():
    parallels = []
    for m in Field.range:
        if m == Field(0): continue
        lines = []
        for c in Field.range:
            lines.append( generateLine(m, c))
        parallels.append(lines)
    return parallels

def generateLine(m, c):
    line = [(m*x + c).id  for x in Field.range]
    return line

 
#
if __name__ == "__main__":
    N = 0
    while N not in {3,5,7,11,13,17,19,23,29,31,37,41}:
        try:
            N = int(input("\nNumber of points (must be prime <42): "))
        except TypeError:
            pass
    
    init_vars()
    parallels = generateAllLines()
    with open(f'desarg{N}.json', 'w') as f:
        json.dump(parallels, f, indent=2)
