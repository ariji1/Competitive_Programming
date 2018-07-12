class Solution(object):
    
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        def my_key(pp):
            return -pp[0],pp[1]
        people.sort(key=my_key)
        for i in range(len(people)):
            if i>=len(people):
                break
            if(people[i][1]==i):
                continue
            tmp=people[i]
            people.pop(i)
            people.insert(tmp[1],tmp)
        return people

S = Solution()
list1 = [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]
list2 = [[12,0],[6,3],[3,4],[9,2], [11,1],[1,5]]
list3 = [[2,4], [5,1], [3,3], [1,5], [4,2], [6,0]]
print(S.reconstructQueue(list1))
print(S.reconstructQueue(list2))
print(S.reconstructQueue(list3))

