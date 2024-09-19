import unittest
class TestRope(unittest.TestCase):
    def testIndex(self):
        r = Rope("howdy yall")
        self.assertEqual(r.index(0), 'h')
        self.assertEqual(r.index(5), ' ')
        self.assertEqual(r.index(9), 'l')
    def testConcat(self):
        r1 = Rope("howdy")
        r2 = Rope(" yall")
        r1.concat(r2)
        self.assertEqual(r1.index(5), ' ')
        self.assertEqual(r1.index(10), 'l')
if __name__ == '__main__':
    unittest.main()

