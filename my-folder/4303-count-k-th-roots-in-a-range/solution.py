class Solution:
    def countKthRoots(self, l: int, r: int, k: int) -> int:
        if k == 1:
            return r - l + 1
        x = 0
        ans = 0
        while True:
            y = x**k
            if y > r:
                break
            if y >= l:
                ans+=1
            x+=1
        return ans
