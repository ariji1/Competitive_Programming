import unittest


def find_rotation_point(words):
    """return the index of the rotation point of a sorted word list"""

    # basically a modified binary search
    index = 0
    n = len(words)
    if n > 1:
        left = 0
        right = n - 1

        while (right - left) > 1:
            if words[left] > words[right]:
                # the pivot is somewhere within this interval
                # but where?
                # split the interval in half
                # check each half for the pivot
                # use the half that contains the pivot
                nexttry = int((left + right) / 2.0 + 0.5)
                if words[nexttry] > words[right]:
                    left = nexttry
                else:
                    right = nexttry
            else:
                # Boy: Do not try and find the pivot. That's
                #      impossible. Instead only try to realize the truth.
                # Neo: What truth?
                # Boy: There is no pivot.
                return left

        if words[left] <= words[right]:
            index = left
        else:
            index = right

    return index
















# Tests

class Test(unittest.TestCase):

    def test_small_list(self):
        actual = find_rotation_point(['cape', 'cake'])
        expected = 1
        self.assertEqual(actual, expected)

    def test_medium_list(self):
        actual = find_rotation_point(['grape', 'orange', 'plum',
                                      'radish', 'apple'])
        expected = 4
        self.assertEqual(actual, expected)

    def test_large_list(self):
        actual = find_rotation_point(['ptolemaic', 'retrograde', 'supplant',
                                      'undulate', 'xenoepist', 'asymptote',
                                      'babka', 'banoffee', 'engender',
                                      'karpatka', 'othellolagkage'])
        expected = 5
        self.assertEqual(actual, expected)

    # Are we missing any edge cases?


unittest.main(verbosity=2)