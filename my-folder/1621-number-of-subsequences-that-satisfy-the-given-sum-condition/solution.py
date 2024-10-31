class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        MOD = 1000000007
        n = len(nums)
        nums = sorted(nums)
        left = 0
        total = 0
        power = [1] * n
        for i in range(1, n):
            power[i] = power[i - 1] * 2 % MOD
        right = n-1
        while left<=right:
            if nums[left]+nums[right]>target:
                right-=1
            else:
                total = (total+power[right-left])%MOD
                left+=1
        return total
           
