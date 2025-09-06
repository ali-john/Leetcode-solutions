class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        n = len(nums)
        ans = float('inf')
        for i in range(n):
            curr = nums[i]
            if curr >=k: 
                ans = 1
                return ans
            else:
                for j in range(i+1,n):
                    curr |= nums[j]
                    if curr>=k:
                        ans = min(ans, j-i + 1)
        
        return ans if ans!=float('inf') else -1


