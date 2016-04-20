from itertools import product

from dobble import dobble

points = lambda line: [i for i,x in enumerate(dobble) if line in x]
m=lambda x,y: list(set(x)&set(y))[0]

def singleton(cls):
    class Singly(cls):
        s = {}
        def __new__(c, *arg): 
            if arg in c.s:
                return c.s[arg]
            self = cls.__new__(c, *arg)
            c.s[arg] = self
            return self
    Singly.__name__ = cls.__name__
    return Singly

@singleton
class Point(object):
    write = staticmethod(lambda num, show='D': '{}{:02}'.format(show, num))
    written = property(lambda self: self.write(self.id, ' ' if self.hidden else 'D'))
    def __init__(self, id):
        self.id = id
        self.lines = dobble[id]
        self.hidden = False
    __and__ = lambda self, other: Line(m(self.lines, other.lines))
    __repr__ = lambda self: '{} {}'.format(self.written, self.lines)
    def set_coords(self, x,y):
        self.xy = self.x, self.y = x,y

@singleton
class Line(object):
    def __init__(self, num):
        self.id = num
        self.points = points(num)
    __and__ = lambda self, other: Point(m(self.points, other.points))
    __repr__ = lambda self: '{}: {}'.format(self.id, map(Point.write, self.points))
    __contains__ = lambda self, pt: pt.id in self.points

class Mod7(int):
    def __new__(cls, num=0):
        num %= 7
        if num>3: num -= 7
        return int.__new__(cls, num)
    __add__ = lambda a,b: Mod7(int.__add__(a,b))
    __radd__ = lambda a,b: Mod7(int.__add__(b,a))
    __sub__ = lambda a,b: Mod7(int.__sub__(a,b))
    __rsub__ = lambda a,b: Mod7(int.__sub__(b,a))
    __mul__ = lambda self, other: Mod7(int.__mul__(self, other))
    __rmul__ = lambda self, other: Mod7(int.__mul__(other, self))

range7 = map(Mod7, range(-3,4))
range7x7 = list(product(range7, range7))

class Plane(dict):
    def __init__(self):
        #Horiz, Vert, O = pts[:3]
        #ideal = Horiz&Vert
        self.Horiz, self.Vert, self.O = pts[:3]
        self.ideal = self.Horiz & self.Vert
        
        print 'Horiz: {}\n Vert: {}\n O: {}\n ideal: {}\n'.format(self.Horiz, self.Vert, self.O, self.ideal)
        
        self[0,0] = self.O
        h0 = self.horiz(self.O)
        self[1,0] = UnitX = Point( min(set(h0.points) - {0,2}) )
        v0 = self.vert(self.O)
        self[0,1] = UnitY = Point( min(set(v0.points) - {1,2}) )
        self.paralelogram((0,0),(1,0), (0,1)) # ->self[1,1]
        # get horizontal and vertical axis, using x=y=k=1,2,3,-3,-2
        self.H0 = {}
        self.V0 = {}
        for k in map(Mod7, range(1,8)):
            self.H0[k] = self[k,0]
            self.V0[k] = self[0,k]
            self.paralelogram((0,1),(1,1), (k,0)) # ->self[k+1,0]
            self.paralelogram((1,0),(1,1), (0,k)) # ->self[0,k+1]
        # fill the rest of the board
        for x,y in range7x7:
            if 0 not in (x,y):
                self.paralelogram((0,0),(x,0), (0,y))
            self[x,y].set_coords(x,y)
    
    horiz = lambda self, pt: pt & self.Horiz
    vert = lambda self, pt: pt & self.Vert
    
    def paralelogram(self, A,B, C):
        (Ax,Ay), (Bx,By), (Cx,Cy) = A,B,C
        D = (Dx,Dy) = (Bx+Cx-Ax, By+Cy-Ay)
        if self.get(D): return
        I = self.ideal & (self[A]&self[B])
        J = self.ideal & (self[A]&self[C])
        BD = self[B] & J
        CD = self[C] & I
        self[D] = BD & CD

    def __repr__(self):
        picture = ''
        for y in range7:
            picture += '\n    '
            for x in range7:
                pt = self.get((x,-y))
                picture += '  {}'.format(pt.written) if pt else '     '
        return picture

    def show(self, pt_or_line):
        if isinstance(pt_or_line, Point):
            self.show_point(pt_or_line)
            return
        line = pt_or_line
        if not isinstance(line, Line):
            line = Line(line)
        self.show_line(line)

    def show_if(self, condition):
        for x,y in range7x7:
            if not condition(x,y):
                self[x,y].hidden = True
        pic = repr(self)
        self.release()
        return pic
    
    def release(self):
        for x,y in range7x7:
            self[x,y].hidden = False

    def show_point(self, pt):
        print self.show_if(lambda x,y: (x,y) == pt.xy)

    def show_line(self, line):
        print self.show_if(lambda x,y: self[x,y] in line)      


pts = map( Point, range(len(dobble)) )
L = lines = {i: Line(i) for i in range(1,58)}

globals().update({pt.written : pt for pt in pts})

if __name__ == '__main__':
    p = Plane()
    print p
