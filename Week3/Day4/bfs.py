import unittest
# from queue import PriorityQueue
from collections import deque


# def bfs_get_path(graph, start_node, end_node):

#     # Find the shortest route in the network between the two users
    

#     return None



def bfs_get_path(graph, start_node, end_node):

    # Find the shortest route in the network between the two users
    #TimeComplexity(O(V+E))
    if graph.get(end_node, None) is None or graph.get(start_node,None) is None:
        raise Exception

    if start_node == end_node:
        return [start_node]

    visited=[]
    previous={}
    queue=[start_node]
    while queue:
        node=queue.pop(0)
        visited.append(node)
        for adj in graph[node]:
            if adj not in visited:
                previous[adj]=node
                queue.append(adj)
                if adj==end_node:
                    spath=[]
                    temp=adj
                    while temp is not None:
                        spath.append(temp)
                        temp=previous.get(temp, None)
                    spath.reverse()
                    return spath

    return None


# print bfs(graph, '1', '11')



# Tests

class Test(unittest.TestCase):

    def setUp(self):
        self.graph = {
            'a': ['b', 'c', 'd'],
            'b': ['a', 'd'],
            'c': ['a', 'e'],
            'd': ['a', 'b'],
            'e': ['c'],
            'f': ['g'],
            'g': ['f'],
        }

    def test_two_hop_path_1(self):
        actual = bfs_get_path(self.graph, 'a', 'e')
        expected = ['a', 'c', 'e']
        self.assertEqual(actual, expected)

    def test_two_hop_path_2(self):
        actual = bfs_get_path(self.graph, 'd', 'c')
        expected = ['d', 'a', 'c']
        self.assertEqual(actual, expected)

    def test_one_hop_path_1(self):
        actual = bfs_get_path(self.graph, 'a', 'c')
        expected = ['a', 'c']
        self.assertEqual(actual, expected)

    def test_one_hop_path_2(self):
        actual = bfs_get_path(self.graph, 'f', 'g')
        expected = ['f', 'g']
        self.assertEqual(actual, expected)

    def test_one_hop_path_3(self):
        actual = bfs_get_path(self.graph, 'g', 'f')
        expected = ['g', 'f']
        self.assertEqual(actual, expected)

    def test_zero_hop_path(self):
        actual = bfs_get_path(self.graph, 'a', 'a')
        expected = ['a']
        self.assertEqual(actual, expected)

    def test_no_path(self):
        actual = bfs_get_path(self.graph, 'a', 'f')
        expected = None
        self.assertEqual(actual, expected)

    def test_start_node_not_present(self):
        with self.assertRaises(Exception):
            bfs_get_path(self.graph, 'h', 'a')

    def test_end_node_not_present(self):
        with self.assertRaises(Exception):
            bfs_get_path(self.graph, 'a', 'h')


unittest.main(verbosity=2)