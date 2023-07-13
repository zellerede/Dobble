#!/usr/bin/env python

""" Generates lines on affine plane based on Octontions with 17 elements
    and writes it in a json file """

import json

### play around with permutations:
# i,j,l,h,k,m,n = 2,3,4,5,6,7,8
# i,j,k,l,m,n,h = 2,3,4,5,6,7,8
# i,j,l,m,k,n,h = 2,3,4,5,6,7,8
i,j,h,m,k,l,n = 2,3,-4,-5,6,-7,8
MUL_TABLE = {
    (i,j): k,  (i,l): n,  (i,h): -m, (i,k): -j, (i,m): h,  (i,n): -l,
    (j,l): h,  (j,h): -l, (j,k): i,  (j,m): -n, (j,n): m,
    (l,h): j,  (l,k): -m, (l,m): k,  (l,n): i,
    (h,k): -n, (h,m): -i, (h,n): k,
    (k,m): -l, (k,n): -h,
    (m,n): -j
}
RANGE = list(range(-8,9))

def extend_mul_table():
    global MUL_TABLE

    for (a,b), r in MUL_TABLE.copy().items():
        MUL_TABLE[(b,a)] = MUL_TABLE[(-b,-a)] = MUL_TABLE[(-a,b)] = MUL_TABLE[(a,-b)] = -r
        MUL_TABLE[(-b,a)] = MUL_TABLE[(-a,-b)] = MUL_TABLE[(b,-a)] = r

    for x in RANGE:
        for i in range(-1, 2):
            MUL_TABLE[(x,i)] = MUL_TABLE[(i,x)] = i*x
        MUL_TABLE.setdefault((x,x), -1)
        MUL_TABLE.setdefault((-x,x), 1)

extend_mul_table()

def mod17(n):
    " -8, ..., -1, 0, +1, ..., +8 "
    return (n+8)%17 -8


class Oct17:
    elements = {}

    def __new__(cls, num):
        elem = cls.elements.get(num)
        if elem is not None: return elem
        elem = object.__new__(cls)
        cls.elements[num] = elem
        return elem

    def __init__(self, num):
        self.num = num
        self.id = num + 9  # for the output 1..17
    
    def __repr__(self):
        r = repr(self.num)
        for k,v in zip('2345678', 'ijlhkmn'):  # apply the correct order
            r = r.replace(k,v)
        return r

    def __mul__(self, other):
        return Oct17(MUL_TABLE[self.num, other.num])

    def __neg__(self):
        return Oct17(-self.num)

    def __add__(self, other):
        return Oct17( mod17(self.num + other.num) )


Oct17.range = list(map(Oct17, RANGE))


def generateAllLines():
    parallels = []
    for m in Oct17.range:
        if m == Oct17(0): continue
        lines = []
        for c in Oct17.range:
            lines.append( generateLine(m, c))
        parallels.append(lines)
    return parallels

def generateLine(m,c):
    line = [(m*x + c).id  for x in Oct17.range]
    return line

def verifyLines(parallels):
    print("Verifying.....")
    lines = []
    for block in parallels:
        lines.extend(block)
    N = len(lines)
    n = len(lines[0])
    n_range = list(range(1, n+1))
    for x in range(N):
        line = lines[x]
        assert all(i in line for i in n_range), f'Permutation error at {x}:\n {line}'
        for y in range(x+1, N): 
            c = sum( 
                a==b for a,b in zip(line, lines[y]) 
            ) 
            assert c<2, f'Indices: {x},{y};  match: {c}\n {lines[x]}\n {lines[y]}' 
 
#
if __name__ == "__main__":
    parallels = generateAllLines()
    verifyLines(parallels)
    with open('oct17.try1.json', 'w') as f:
        json.dump(parallels, f)
