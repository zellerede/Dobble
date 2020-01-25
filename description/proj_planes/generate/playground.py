
from itertools import permutations

def init(n):
    global N, R, E, E1, comp, inv, nbr
    if n>20:
        raise ValueError("Forget about big numbers")
    N = n
    R = tuple(range(N))
    E = {p for p in permutations(R) if sum(p[x]==x for x in R) <= 1}
    E1 = E | {R}
    comp = lambda p,q,r=R: tuple(p[q[x]] for x in r)
    inv = lambda p: tuple(p.index(x) for x in R)
    nbr = lambda p: {comp(p,e) for e in E} & E  
    # nbr (set of neighbors) to be optimized,
    # using cycle decomposition and conjugate invariance of E

def nbrs(S):
    q = E.copy()
    for i,p in enumerate(S): 
        q &= nbr(p) 
        n = len(q) 
        if n <= 1000: print(i,n)
    return q

def cycles(p):
    n = len(p)  # should be N
    c = []
    indices = set(range(n))
    while indices:
        x = indices.pop()
        cycle_start = x
        cycle = [x]
        x = p[x]
        while x != cycle_start:
            cycle.append(x)
            indices.remove(x)
            x = p[x]
        c.append(cycle)
    c.sort(key=len)
    return c

def dedicated_reordering(p):
    return sum(cycles(p), [])

def dedicated_conjugate(p):
    g = dedicated_reordering(p)
    return comp(inv(g),p,g)

# pE = {pe : e in E} = gqg^(-1)E = g(qE)g^(-1)
# pE & E = gqEg^{-1} & gEg^{-1} = g(qE & E)g^{-1}
