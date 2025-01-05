class Solution:
    def maxLength(self, nums: List[int]) -> int:
        
        def lcm(a, b):
            return a * b // gcd(a, b)

        n = len(nums)
        l = 0
        
        for i in range(n):
            curr_g = nums[i]
            curr_l = nums[i]
            curr_p = nums[i]
            
            for j in range(i, n):
                if i != j:
                    curr_g = gcd(curr_g, nums[j])
                    curr_l = lcm(curr_l, nums[j])
                    curr_p *= nums[j]
                
                if curr_p == curr_l * curr_g:
                    l = max(l, j - i + 1)
        
        return l
