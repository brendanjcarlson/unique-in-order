import unittest
from whiteboard import solution

class WhiteboardTest(unittest.TestCase):
    def test_1(self):
        self.assertEqual(solution('aAbbBBBBbbbbcccCCCcc'), ['a','A','b','B','b','c','C','c'])

    def test_2(self):
        self.assertEqual(solution('abcdefg'), ['a','b','c','d','e','f','g'])

    def test_3(self):
        self.assertEqual(solution('aabbccddeee'), ['a','b','c','d','e'])

    def test_4(self):
        self.assertEqual(solution('1233322233222111232312333'), ['1','2','3','2','3','2','1','2','3','2','3','1','2','3'])

    def test_5(self):
        self.assertEqual(solution(''), [])

    def test_6(self):
        self.assertEqual(solution('codingtemple'), ['c','o','d','i','n','g','t','e','m','p','l','e'])

if __name__ == '__main__':
    unittest.main()