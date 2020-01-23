from itertools import permutations

N = 8

def comp(p,q):
    return tuple(p[x] for x in q)

def inv(p):
    return tuple(p.index(x) for x in RANGE)


RANGE = tuple(range(N))
PERMS = list(permutations(RANGE))
E = [p for p in PERMS if sum(p[i]==i for i in RANGE)<=1]

points = set(map(hash, E))

def neighbors(p, points=points):
    return {hash(comp(p,e)) for e in E} & points

E.sort(key=lambda p: len(neighbors(p)))


with open(f'graph{N}.clq', 'w') as f: 
    print(f"p edge {len(E)}", file=f)
    for i,p in enumerate(E):
        for q in E:
            r = comp(p,q)
            if r in E:
                print(f"e {i} {PP[r]}", file=f)


################

def do_graph(N): 
    R=tuple(range(N)) 
    P=list(permutations(R)) 
    E = [p for p in P if sum(p[i]==i for i in R) <= 1] 
    EE = {p:i for i,p in enumerate(E)} 
    with open(f'graph{N}.clq', 'w') as f:  
        print(f"p edge {len(E)}", file=f) 
        for i,p in enumerate(E): 
            for q in E: 
                r = EE.get(comp(p,q)) 
                if r: 
                    print(f"e {i} {r}", file=f)

# mcqd is working up to N=6, but for N=7 it's already extremely slow for finding maximal clique

######################

def cycles(p):
    cyc = []
    pl = list(enumerate(p))
    while pl:
        n = 1
        x,y = pl.pop(0)
        while y!=x:
            n += 1
            z = p[y]
            pl.remove((y,z))
            y = z
        cyc.append(n)
    return tuple(sorted(cyc))

###
# amateur approach!!!
Cset = set()
for p in permutations(R): 
    cyc = cycles(p) 
    if cyc not in Cset: 
        C.append(p) 
        Cset.add(cyc)

###
# to count conjugate classes,
# just decompose 12 in all possible (77) ways  by positive integers (1+11, 1+1+10, ...)

CYC = [set(), {(1,)}]

def calcNextCyc():
    n = len(CYC)
    decomps = {(n,)}
    for i in range(1, n+1):
        decomps |= {tuple(sorted(list(c)+[i])) for c in CYC[n-i]}
    CYC.append(decomps)

for i in range(11): calcNextCyc()

Ecyc = {t for t in CYC[12] if t.count(1)<=1}


C1 = [] 
for cyc in Ecyc: 
    p = [] 
    x = 0 
    for l in cyc: 
        start = x 
        for i in range(l-1): 
            x += 1 
            p.append(x) 
        p.append(start) 
        x += 1 
    C1.append(tuple(p)) 

# this results in
C1 = [
 (0, 2, 3, 4, 1, 6, 7, 8, 9, 10, 11, 5),
 (1, 2, 3, 0, 5, 6, 7, 8, 9, 10, 11, 4),
 (1, 2, 3, 4, 5, 0, 7, 8, 9, 10, 11, 6),
 (0, 2, 1, 4, 5, 6, 7, 8, 9, 10, 11, 3),
 (1, 0, 3, 4, 2, 6, 7, 8, 9, 10, 11, 5),
 (0, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 1),
 (1, 2, 0, 4, 5, 3, 7, 8, 6, 10, 11, 9),
 (0, 2, 1, 4, 3, 6, 7, 8, 9, 10, 11, 5),
 (0, 2, 1, 4, 5, 3, 7, 8, 9, 10, 11, 6),
 (1, 0, 3, 2, 5, 6, 7, 8, 9, 10, 11, 4),
 (1, 0, 3, 2, 5, 4, 7, 6, 9, 8, 11, 10),
 (0, 2, 1, 4, 3, 6, 5, 8, 7, 10, 11, 9),
 (0, 2, 3, 1, 5, 6, 7, 4, 9, 10, 11, 8),
 (1, 2, 0, 4, 5, 3, 7, 8, 9, 10, 11, 6),
 (0, 2, 3, 1, 5, 6, 7, 8, 9, 10, 11, 4),
 (1, 0, 3, 2, 5, 4, 7, 8, 9, 10, 11, 6),
 (1, 0, 3, 2, 5, 4, 7, 6, 9, 10, 11, 8),
 (1, 0, 3, 4, 5, 2, 7, 8, 9, 10, 11, 6),
 (0, 2, 1, 4, 5, 3, 7, 8, 6, 10, 11, 9),
 (1, 0, 3, 2, 5, 6, 7, 4, 9, 10, 11, 8),
 (1, 0, 3, 4, 5, 6, 7, 8, 9, 10, 11, 2),
 (1, 2, 0, 4, 5, 6, 7, 8, 9, 10, 11, 3),
 (0, 2, 1, 4, 3, 6, 7, 5, 9, 10, 11, 8),
 (1, 0, 3, 2, 5, 6, 4, 8, 9, 10, 11, 7),
 (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 0),
 (1, 0, 3, 4, 2, 6, 7, 5, 9, 10, 11, 8),
 (1, 0, 3, 2, 5, 4, 7, 8, 6, 10, 11, 9),
 (0, 2, 1, 4, 3, 6, 5, 8, 9, 10, 11, 7),
 (1, 0, 3, 4, 5, 6, 2, 8, 9, 10, 11, 7),
 (1, 2, 3, 4, 0, 6, 7, 8, 9, 10, 11, 5),
 (0, 2, 3, 4, 5, 1, 7, 8, 9, 10, 11, 6),
 (1, 2, 3, 0, 5, 6, 7, 4, 9, 10, 11, 8),
 (0, 2, 3, 1, 5, 6, 4, 8, 9, 10, 11, 7),
 (1, 2, 0, 4, 5, 6, 3, 8, 9, 10, 11, 7),
 (0, 2, 1, 4, 5, 6, 3, 8, 9, 10, 11, 7)
]