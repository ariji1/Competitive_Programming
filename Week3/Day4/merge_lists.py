import unittest


# def merge_lists(my_list, alices_list):

#     # Combine the sorted lists into one large sorted list
    

#     return []
def merge_lists(listi, listj):
    """merge these two sorted lists"""

    sortd = []
    i = 0
    j = 0
    leni = len(listi)
    lenj = len(listj)
    while i < leni or j < lenj:
        ith = listi[i] if i < leni else float('inf')
        jth = listj[j] if j < lenj else float('inf')
        if ith < jth:
            i += 1
            sortd.append(ith)
        else:
            j += 1
            sortd.append(jth)
    return sortd



# Tests

class Test(unittest.TestCase):

    def test_both_lists_are_empty(self):
        actual = merge_lists([], [])
        expected = []
        self.assertEqual(actual, expected)

    def test_first_list_is_empty(self):
        actual = merge_lists([], [1, 2, 3])
        expected = [1, 2, 3]
        self.assertEqual(actual, expected)

    def test_second_list_is_empty(self):
        actual = merge_lists([5, 6, 7], [])
        expected = [5, 6, 7]
        self.assertEqual(actual, expected)

    def test_both_lists_have_some_numbers(self):
        actual = merge_lists([2, 4, 6], [1, 3, 7])
        expected = [1, 2, 3, 4, 6, 7]
        self.assertEqual(actual, expected)

    def test_lists_are_different_lengths(self):
        actual = merge_lists([2, 4, 6, 8], [1, 7])
        expected = [1, 2, 4, 6, 7, 8]
        self.assertEqual(actual, expected)


unittest.main(verbosity=2)