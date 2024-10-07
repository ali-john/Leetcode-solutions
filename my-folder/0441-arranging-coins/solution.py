class Solution:
    def arrangeCoins(self, n: int) -> int:
        if n==1:
            return 1
        left = 1
        right = n
        while left<right:
            mid = (left+right)//2
            num = (mid*(mid+1))//2
            if num>n:
                right = mid
            elif num==n:
                return mid
            else:
                left = mid+1
        return left-1
        
