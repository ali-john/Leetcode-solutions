class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        min_len = float('inf')

        left = 0
        right = 0

        running_total = 0

        while right < n:
            running_total+=nums[right]

            while left<=right and running_total >= target:
                min_len = min(min_len, (right-left)+1)
                running_total-=nums[left]

                left+=1
            right+=1
        
        return min_len if min_len != float('inf') else 0

                


