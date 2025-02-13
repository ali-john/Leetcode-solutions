class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        min_window = float('inf')
        ones = nums.count(1)
        if ones: return n-ones
        for i in range(n):
            g = nums[i]
            for j in range(i+1,n):
                g = gcd(g,nums[j])
                if g ==1:
                    min_window = min(min_window,(j-i))
        if min_window == float('inf'): return -1
        op = min_window + n-1
        return op

