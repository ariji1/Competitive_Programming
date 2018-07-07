# Time:  O(n)
# Space: O(n)

class Solution(object):
    def minSwapsCouples(self, row):
        """
        :type row: List[int]
        :rtype: int
        """
        N = len(row)//2
        couples = [[] for _ in range(N)]
        for seat, num in enumerate(row):
            couples[num//2].append(seat//2)
        adj = [[] for _ in range(N)]
        for couch1, couch2 in couples:
            adj[couch1].append(couch2)
            adj[couch2].append(couch1)
            
        result = 0
        for couch in range(N):
            if not adj[couch]: continue
            couch1, couch2 = couch, adj[couch].pop()
            while couch2 != couch:
                result += 1
                adj[couch2].remove(couch1)
                couch1, couch2 = couch2, adj[couch2].pop()
        return result
s = Solution()
print(s.minSwapsCouples([0,2,1,3]))
print(s.minSwapsCouples([3,2,0,1]))
print(s.minSwapsCouples([1,3,4,0,2,5]))
print(s.minSwapsCouples([3,2,0,1]))
print(s.minSwapsCouples([3,30,50,90,16,91,65,18,61,58]))
print(s.minSwapsCouples([3,1,5,4,6,2]))
print(s.minSwapsCouples([55,37,19,46,66,32,7,81,33,76,00,28,92,26,99,6,56,29,17,52,90,79,91,83,12,40,82,84,2,21,11,68,98,34,73,10,57,58,64,36]))
print(s.minSwapsCouples([1,0]))
print(s.minSwapsCouples([50,23,76,19,16,70,35,68,41,49,99,71,59,95,89,33,22,7,54,83,24,0,18,64,11,14,77,26,42,21,82,1,97,52,65,79,37,62,60,91,98,4,88,36,51,20,85,90,29,84,93,13,80,6,55,48,2,40,46,81,30,3,94,38,27,31,53,86,32,96,8,58,73,5]))