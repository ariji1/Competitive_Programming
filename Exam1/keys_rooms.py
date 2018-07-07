
class Solution(object):
    def visitAllRooms(self, rooms):
        lookup = set([0])
        stack = [0]
        while stack:
            node = stack.pop()
            for nei in rooms[node]:
                if nei not in lookup:
                    lookup.add(nei)
                    if len(lookup) == len(rooms):
                        return True
                    stack.append(nei)
        return len(lookup) == len(rooms)

s = Solution()
print(s.visitAllRooms([[1], [0,2], [3]]))
print(s.visitAllRooms([[1,3], [3,0,1], [2], [0]]))
print(s.visitAllRooms([[1], [0,2], [3]] ))
print(s.visitAllRooms([[1,3], [3,0,1], [2], [0]]))
print(s.visitAllRooms([[1,2,3], [0], [0], [0]] ))