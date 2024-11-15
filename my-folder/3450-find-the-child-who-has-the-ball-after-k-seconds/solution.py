class Solution:
    def numberOfChild(self, n: int, k: int) -> int:
        child  = range(n)

        index = 0
        forward = True
        while k:
            if index==n-1:
                forward = False
            elif index==0:
                forward = True

            if forward:
                index+=1
            else:
                index-=1

            k-=1
        return index
            
