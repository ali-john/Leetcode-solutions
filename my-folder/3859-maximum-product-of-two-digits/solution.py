class Solution:
    def maxProduct(self, n: int) -> int:
        n_str = str(n)
        digits = [int(num) for num in n_str]
        digits.sort()
        max1, max2 = digits[-1], digits[-2]
        return max1*max2
        

