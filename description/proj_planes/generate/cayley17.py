#!/usr/bin/env python

""" Generates lines on affine plane based on Octontions with 17 elements
    and writes it in a json file """

import json

### later: play around with permutations
i,j,h,ij,hi,hj,hij = 2,3,4,6,8,-5,7  # 4*3 = 12 = -5, 4*6 = 24 = 7  mod 17

MUL_TABLE = {
    (i,j): ij,   (i,h): -hi,   (i,ij): -j,   (i,hi): h,   (i,hj): hij, (i,hij): -hj,
    (j,h): -hj,  (j,ij): i,    (j,hi): -hij, (j,hj): h,   (j,hij): hi,
    (h,ij): hij, (h,hi): -i,   (h,hj): -j,   (h,hij): -ij,
    (ij,hi): hj, (ij,hj): -hi, (ij,hij): h,
    (hi,hj): ij, (hi,hij): -j,
    (hj,hij): i
}

RANGE = list(range(-8,9))
N = len(RANGE)  # 17

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


class C17:
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
        for k,v in zip('2345678', ('i', 'j', 'h', '-hj', 'ij', 'hij', 'hi')):
            r = r.replace(k,v).replace('--','')
        return r

    def __mul__(self, other):
        return C17(MUL_TABLE[self.num, other.num])

    def __neg__(self):
        return C17(-self.num)

    def __add__(self, other):
        return C17( mod17(self.num + other.num) )


C17.range = list(map(C17, RANGE))

O,E,i,j,h,ij,hi,hj,hij = map(C17, (0,1,i,j,h,ij,hi,hj,hij))
k,hk,hji = ij, hij, -hij
ji,ih,jh,ijh = -ij, -hi, -hj, -hij

###
### Towards projective plane generation
###

def generateAllLines():
    parallels = []
    for m in C17.range:
        if m == C17(0): continue
        lines = []
        for c in C17.range:
            lines.append( generateLine(m, c))
        parallels.append(lines)
    return parallels

def generateLine(m,c):
    line = [(m*x + c).id  for x in C17.range]
    return line

def drawLine(m,c=O):
    line = generateLine(m,c)
    for y in reversed(C17.range):
        if m == O:
           row = '<>'*N if y == c else ' .' *N
        else:
            x = line.index(y.id)
            row = ' .'*x + '<>' + ' .'*(N-x-1)
        print(row)

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
            if c>=2:
              print(f'Indices: {x},{y};  match: {c}\n {lines[x]}\n {lines[y]}')

def checkAssociativity():
    range = C17.range[-7:]
    range[3] = -range[3]  # hj
    ok = nok = 0
    for a in range:
        for b in range:
            for c in range:
                left,right = (a*b)*c, a*(b*c)
                if left==right:
                    ok += 1
                else:
                    nok += 1
                    print(f' ********   ({a},{b},{c}):     \t({a}*{b})*{c} = {left} != {right} = {a}*({b}*{c})')
    return ok,nok

#
if __name__ == "__main__":
    parallels = generateAllLines()
    verifyLines(parallels)
    with open('C17.try1.json', 'w') as f:
        json.dump(parallels, f)
