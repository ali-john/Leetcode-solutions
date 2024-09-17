class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        table = collections.Counter()
        table[0] = 1
        cumm = 0
        total = 0
        for i in range(n):
            cumm+=nums[i]

            if cumm - k in table:
                total+= table[cumm-k]
            
            table[cumm]+=1
        
        return total
            

