class Solution:
    def removeZeros(self, n: int) -> int:
        str_n = str(n)
        ans = []
        for char in str_n:
            if char != '0':
                ans.append(char)
        return int("".join(ans))
        
