import unittest


# def reverse_words(message):

#     # Decode the message by reversing the words
    

#     pass


def reverse_words(message):
    """reverse the message 'in place' in a mutable byte array"""

    b = bytearray(message)

    # reverse the entire bytearray in place
    reverse_bytes(b, 0, len(b))

    # now walk through the byte array finding words and the reverse
    # each word in place

    start = 0
    space = b.find(" ")
    while space != -1:
        reverse_bytes(b, start, space - start)

        start = space + 1
        space = b.find(" ", start)
    else:
        # reverse the unreversed remainder
        reverse_bytes(b, start, len(b) - start)

    return str(b)


def reverse_bytes(b, start, length):
    """reverses the bytes in array b, starting at start, for length bytes"""
    for i in range(length / 2):
        begin = start + i
        finish = start + (length - 1) - i
        (b[begin], b[finish]) = (b[finish], b[begin])
    return None













# Tests

class Test(unittest.TestCase):

    def test_one_word(self):
        message = list('vault')
        reverse_words(message)
        expected = list('vault')
        self.assertEqual(message, expected)

    def test_two_words(self):
        message = list('thief cake')
        message = list(reverse_words(message))
        expected = list('cake thief')
        self.assertEqual(message, expected)

    def test_three_words(self):
        message = list('one another get')
        message = list(reverse_words(message))
        expected = list('get another one')
        self.assertEqual(message, expected)

    def test_multiple_words_same_length(self):
        message = list('rat the ate cat the')
        message = list(reverse_words(message))
        expected = list('the cat ate the rat')
        self.assertEqual(message, expected)

    def test_multiple_words_different_lengths(self):
        message = list('yummy is cake bundt chocolate')
        message = list(reverse_words(message))
        expected = list('chocolate bundt cake is yummy')
        self.assertEqual(message, expected)

    def test_empty_string(self):
        message = list('')
        reverse_words(message)
        expected = list('')
        self.assertEqual(message, expected)


unittest.main(verbosity=2)