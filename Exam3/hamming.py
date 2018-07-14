class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        biX = bin(x)[2:]
        biY = bin(y)[2:]
        ll = max(len(biX),len(biY))
        sl = min(len(biX),len(biY))
        if len(biX)<=len(biY):
            biX = '0'*(ll-sl) + biX
        else:
            biY = '0'*(ll-sl) + biY
        n = 0
        for i in range(ll):
            if biX[i] != biY[i]:
                n += 1
        return n
s =  Solution()

print(s.hammingDistance(25,30))
print(s.hammingDistance(1,4))
print(s.hammingDistance(100,250))
print(s.hammingDistance(1,30))
print(s.hammingDistance(0,255))
# print(s.hammingDistance(25,30))