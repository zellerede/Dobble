#!/usr/bin/env python

""" Generates lines on affine plane based on a NearField of 9 elements
    and writes it in a json file """

import json

k,i,j = 2,3,4
MUL_TABLE = {
    (i,i): -1, (i,k): -j, (i,j): k,
    (k,i): j,  (k,k): -1, (k,j): -i,
    (j,i): -k, (j,k): i,  (j,j): -1
}

def extend_mul_table():
    global MUL_TABLE
    for y in range(-4, 5):
        for x in range(-4, 5):
            if (-1 <= x <= 1) or (-1 <= y <= 1):
                MUL_TABLE[(x,y)] = x*y
                continue
            if (x,y) not in MUL_TABLE:
                positive = (x>0) == (y>0)
                pos_result =  MUL_TABLE[(abs(x), abs(y))]
                MUL_TABLE[(x,y)] = pos_result if positive else -pos_result

extend_mul_table()

def mod3(n):
    " -1, 0, +1 "
    return (n+1)%3 -1

class Near9:
    elements = {}

    def __new__(cls, num):
        elem = cls.elements.get(num)
        if elem is not None: return elem
        elem = object.__new__(cls)
        cls.elements[num] = elem
        return elem

    def __init__(self, num):
        self.num = num
        self.id = num + 4  # num +9*(num<0)  # to keep 0..4
    
    def __repr__(self):
        return repr(self.num).replace('2','h').replace('3','i').replace('4','j')

    def __mul__(self, other):
        return Near9(MUL_TABLE[self.num, other.num])

    def __neg__(self):
        return Near9(-self.num)

    def __add__(self, other):
        b1, b2 = mod3(self.num), mod3(other.num)
        a1, a2 = (self.num - b1) // 3, (other.num - b2) // 3
        return Near9( mod3(a1+a2) * 3 + mod3(b1+b2) )

Near9.range = list(map(Near9, range(-4,5)))


def generateAllLines():
    parallels = []
    for m in Near9.range:
        if m == Near9(0): continue
        lines = []
        for c in Near9.range:
            lines.append( generateLine(m, c))
        parallels.append(lines)
    return parallels

def generateLine(m,c):
    line = [(m*x + c).id  for x in Near9.range]
    return line

 
#
if __name__ == "__main__":
    parallels = generateAllLines()
    with open('near9.json', 'w') as f:
        json.dump(parallels, f)