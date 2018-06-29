import unittest


# def can_two_movies_fill_flight(movie_lengths, flight_length):

#     # Determine if two movie runtimes add up to the flight length
    

#     return False
# def can_two_movies_fill_flight(flight_length, movie_lengths):
#     """return true if two movies sum up to a flight length duration"""

#     lengths = {}  # a 1:many map of lengths to their movies
#     for length in movie_lengths:
        
#         # put each length of a movie into a hash table as we scan over
#         # all the movies (by length) see if the complement movie is
#         # already in lengths.  by the time we reach the end of the
#         # movies by lengths every movie has been checked for its
#         # complement and since we check before insertion, no one has
#         # to watch the same movie twice.

#         complement = flight_length - length
#         if complement in lengths:
#             return True

#         lengths[length] = True

#     return False

def can_two_movies_fill_flight(movie_lengths, flight_length):
    movie_lengths_seen = set()
    for i in movie_lengths:
        second_movie_length = flight_length-i
        if second_movie_length in movie_lengths_seen:
            return True
        movie_lengths_seen.add(i)















# Tests

class Test(unittest.TestCase):

    def test_short_flight(self):
        result = can_two_movies_fill_flight([2, 4], 1)
        self.assertFalse(result)

    def test_long_flight(self):
        result = can_two_movies_fill_flight([2, 4], 6)
        self.assertTrue(result)

    def test_one_movie_half_flight_length(self):
        result = can_two_movies_fill_flight([3, 8], 6)
        self.assertFalse(result)

    def test_two_movies_half_flight_length(self):
        result = can_two_movies_fill_flight([3, 8, 3], 6)
        self.assertTrue(result)

    def test_lots_of_possible_pairs(self):
        result = can_two_movies_fill_flight([1, 2, 3, 4, 5, 6], 7)
        self.assertTrue(result)

    def test_only_one_movie(self):
        result = can_two_movies_fill_flight([6], 6)
        self.assertFalse(result)

    def test_no_movies(self):
        result = can_two_movies_fill_flight([], 2)
        self.assertFalse(result)


unittest.main(verbosity=2)