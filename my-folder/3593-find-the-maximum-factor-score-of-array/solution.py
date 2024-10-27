class Solution:
    def maxScore(self, nums: List[int]) -> int:
        
        def lcm(a, b):
            return a * (b // gcd(a, b))

        n = len(nums)
        
        overall_gcd = nums[0]
        overall_lcm = nums[0]
        for num in nums:
            overall_gcd = gcd(overall_gcd, num)
            overall_lcm = lcm(overall_lcm, num)

        max_factor_score = overall_gcd * overall_lcm

        for i in range(n):
            temp_gcd = 0
            temp_lcm = 1
            
            for j in range(n):
                if i != j:
                    temp_gcd = gcd(temp_gcd, nums[j])
                    temp_lcm = lcm(temp_lcm, nums[j])
                    
            max_factor_score = max(max_factor_score, temp_gcd * temp_lcm)

        return max_factor_score
                
                
