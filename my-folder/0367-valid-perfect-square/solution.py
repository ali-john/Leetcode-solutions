class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num==1:
            return True
        
        left = 1
        right  = num//2

        while left<=right:
            mid = (right + left)//2
            square = mid**2
            if square == num:
                return True
            elif square>num:
                right = mid-1
            else:
                left = mid+1
        return False


