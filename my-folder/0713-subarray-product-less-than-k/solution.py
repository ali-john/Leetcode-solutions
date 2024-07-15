class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        l = 0
        product = 1
        result = 0
        for r in range(len(nums)):
            product*=nums[r]

            while l<=r and product>=k:
                product = product // nums[l]
                l+=1
            result+= (r-l+1)
        return result
            

        
        
            
            
        

        

        
