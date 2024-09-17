class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        n = len(nums)
        table = collections.Counter()
        table[0] = 1
        cumm = 0
        total = 0
        for i in range(n):
            cumm+=nums[i]

            if cumm - goal in table:
                total+= table[cumm-goal]
            
            table[cumm]+=1
        
        return total
