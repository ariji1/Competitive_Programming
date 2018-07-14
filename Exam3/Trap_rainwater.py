class Solution:
    # @param A, a list of integers
    # @return an integer
    def trap(self, A):
        if not A:
            return 0
        
        highestLeftSoFar=[]
        highestRightSoFar=[]
        
        for i in range(len(A)):
            highestLeftSoFar.append(A[i] if i==0 else max(A[i], highestLeftSoFar[-1]))
        
        for i in range(len(A)-1, -1, -1):
            highestRightSoFar.insert(0,A[i] if i==len(A)-1 else max(A[i], highestRightSoFar[0]))
            
        totalVolume=0
        for i, currentHeight in enumerate(A):
            minSideHeight=min(highestLeftSoFar[i], highestRightSoFar[i])
            if minSideHeight>currentHeight:
                totalVolume+=(minSideHeight-currentHeight)*1
                
        return totalVolume
s = Solution()
a = [[0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1],[0, 1, 0, 2, 1, 0, 1],[0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1],[0, 1, 0, 2, 1, 0, 5, 1, 0, 2],[0, 1, 0, 5, 1, 0, 2],[0, 5, 1, 3, 4, 0, 1]]  

for la in a:
     print(s.trap(la))
