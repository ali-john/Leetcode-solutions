class Solution:
    def longestAlternatingSubarray(self, nums: List[int], threshold: int) -> int:
        ans = 0
        n = len(nums)
        for i in range(n):
            if nums[i]%2==0 and nums[i]<=threshold:
                ans = max(ans,1)
                for j in range(i+1,n):
                    if nums[j]%2!=nums[j-1]%2 and nums[j]<=threshold:
                        ans = max(ans,(j-i+1))
                    else:
                        break
        return ans
