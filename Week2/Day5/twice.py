import unittest


# def find_repeat(numbers_list):

#     # Find the number that appears twice
    

#     return 0

def find_repeat(ints):
    """find the number in ints that appears twice"""

    n = len(ints)
    # n ints, so the list is
    # 1..(n-1) + some duplicated number
    # = ((n-1) * (1 + n - 1) / 2)
    # = ((n-1) * (n) / 2)
    # = ((n-1) * (n / 2.0)
    gauss = int((n - 1) * (n / 2.0))
    total = sum(ints)
    dupe = total - gauss
    return dupe





# Tests

class Test(unittest.TestCase):

    def test_short_list(self):
        actual = find_repeat([1, 2, 1])
        expected = 1
        self.assertEqual(actual, expected)

    def test_medium_list(self):
        actual = find_repeat([4, 1, 3, 4, 2])
        expected = 4
        self.assertEqual(actual, expected)

    def test_long_list(self):
        actual = find_repeat([1, 5, 9, 7, 2, 6, 3, 8, 2, 4])
        expected = 2
        self.assertEqual(actual, expected)


unittest.main(verbosity=2)