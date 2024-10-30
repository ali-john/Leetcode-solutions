class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)

        left = 0
        total = 0
        max_count = 0
        max_element = max(nums)

        for right in range(n):
            if nums[right]==max_element:
                max_count+=1
            
            while max_count>=k and left<=right:
                total+=(n-right)
                if nums[left]==max_element:
                    max_count-=1
                
                left+=1
        return total
                


