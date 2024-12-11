class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        n = len(nums)
        nums.sort()

        left = 0
        right = 0
        max_ans = float('-inf')

        while right<n:
            while (nums[right] - nums[left]) > 2*k:
                left+=1
            
            max_ans = max(max_ans,(right-left+1))
            right+=1
        return max_ans
            
            


