from collections import defaultdict
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        sum_n = (n*(n+1))//2
        total_s = 0
        for num in nums:
            total_s+=num
        
        return sum_n - total_s
        
       
        

            


        
