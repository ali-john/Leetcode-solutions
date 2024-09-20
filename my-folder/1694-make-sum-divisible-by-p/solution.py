class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        table = {0:-1}
        need = sum(nums)%p # we need to remove this sum(subarry)%p from whole array

        if need==0:
            return 0
        
        min_length = len(nums)
        prefix_sum = 0
        for i,num in enumerate(nums):
            prefix_sum+=num 
            curr = prefix_sum%p
            
            want = (curr - need)%p
            if want in table:
                min_length = min(min_length, i-table[want])
            
            table[curr] = i
        
        return min_length if min_length<len(nums) else -1




