import unittest
import dobble_plane as _D

class TestDobblePlane(unittest.TestCase):
    def test_seen_49_points(self):
        self.assertEqual( 49, len(set(repr(_D.p).split())) )

    def test_horiz_lines(self):
        for y in _D.range7:
            self.assertTrue( (_D.p[0,y] & _D.p[1,y]).id  in  _D.dobble[0] )
    
    def test_vert_lines(self):
        for x in _D.range7:
            self.assertTrue( (_D.p[x,-2] & _D.p[x,1]).id  in  _D.dobble[1] )

if __name__ == '__main__':
    _D.main()
    unittest.main()