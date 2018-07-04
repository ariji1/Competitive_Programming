import unittest


# def reverse(list_of_chars):

#     # Reverse the input list of chars in place
    

#     pass


def reverse(l):
    """reverse the list in place"""

    n = len(l)
    for i in range(n / 2):
        (l[i], l[n - i - 1]) = (l[n - i - 1], l[i])

    # I like my solution that uses these in place, no need for a
    # temp val swap but at hacker news, someone says the "correct"
    # way is, and I think they are right, to use extended slices
    # as:

    # return l[::-1]

    return l


# def reverse(input):
#     length = len(input)
#     reverse_str = []
#     while length > 0:
#         reverse_str.append(input[length-1])
#         length-=1
#     return "".join(reverse_str)















# Tests

class Test(unittest.TestCase):

    def test_empty_string(self):
        list_of_chars = []
        reverse(list_of_chars)
        expected = []
        self.assertEqual(list_of_chars, expected)

    def test_single_character_string(self):
        list_of_chars = ['A']
        reverse(list_of_chars)
        expected = ['A']
        self.assertEqual(list_of_chars, expected)

    def test_longer_string(self):
        list_of_chars = ['A', 'B', 'C', 'D', 'E']
        list_of_chars = reverse(list_of_chars)
        expected = ['E', 'D', 'C', 'B', 'A']
        self.assertEqual(list_of_chars, expected)


unittest.main(verbosity=2)