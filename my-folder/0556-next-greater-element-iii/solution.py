class Solution:
    def nextGreaterElement(self, n: int) -> int:
        nums = [d for d in str(n)]
        l  = len(nums)

        if l == 1: return -1

        i = l - 2
        while i >= 0 and nums[i] >= nums[i+1]: i-=1
        if i < 0: return -1

        j = l - 1
        while nums[j] <= nums[i]:
            j -= 1
        
        nums[j] , nums[i] = nums[i], nums[j]
        nums[i+1: ] = reversed(nums[i+1: ])
        ans = int("".join(nums))
        return ans if ans< 2**31 else -1


