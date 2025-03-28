class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        ones = nums.count(1)

        if ones:
            return n - ones
        
        # check if you can make 1s
        min_window = float('inf')
        for i in range(n):
            g = nums[i]
            for j in range(i+1,n):
                g = gcd(g,nums[j])
                if g == 1:
                    min_window = min(min_window, (j-i))
        if min_window == float('inf'): return -1
        return min_window + n-1
            
# test case
# [6, 10, 15] # we need to check if we can make the whole window gcd == 1
# [6, 2, 15]
# [6,2,1]
# [6,1,1]
# [1,1,1]

