class Solution:
    def countAlternatingSubarrays(self, nums: List[int]) -> int:

        n = len(nums)
        left = 0
        ans = len(nums)
        right = 0
        while left<n:
            right = left+1
            while right<n and nums[right-1]!=nums[right]:
                right+=1

            length = (right-left)
            ans+=(length*(length-1))//2
            left = right
            
        return ans
            
            
                
                
                
            
