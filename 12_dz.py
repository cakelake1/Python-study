import unittest
from random import randint
from dz_sort_massive_12_dz import get_min_max

class GetMinMaxTests(unittest.TestCase):
    def test_correct_max(self):
        self.assertEqual(get_min_max([1,2,4,3,1], False), 4)

    def test_correct_min(self):
        self.assertEqual(get_min_max([1,2,4,3,1], True), 1)

    def setUp(self):
        self.getMinMax = get_min_max([1,2,4,3,1], False)

    def tearDown(self):
        get_min_max([1,2,4,3,1], False)


    def test_random( self):
        for i in range(100000):
            x = randint(-25,+25)
            y = randint(-25,+25)
            w = randint(-25,25)
            s = randint(-25,25)
            z = get_min_max([x,y,w,s], False)
            self.assertEqual(z, get_min_max([x, y, w, s], False))
    
    def test_null(self):
        self.assertEqual(get_min_max([0,0,0,0,0], False), 0)
        try:
            d = get_min_max([0,0,0,0,0])
            self.assertEqual(d, False)
            self.assertTrue(False) # fail
        except:
            pass # success

    def test_max (self):
        self.assertEqual(get_min_max([9223372036854775808,9223372036854775809,-9223372036854775808,9223372036854775820, -8223372036854775808], False), 9223372036854775820)

    def test_min (self):
        self.assertEqual(get_min_max([9223372036854775808,9223372036854775809,-9223372036854775808,9223372036854775820, -8223372036854775808], True), -9223372036854775808)

if __name__ == '__main__':
    unittest.main()