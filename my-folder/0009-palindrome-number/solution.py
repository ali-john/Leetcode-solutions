class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        x = str(x)
        n = len(x)
        for i in range(n//2):
            start = x[i]
            end = x[n-i-1]
            if start!=end:
                return False
        return True

