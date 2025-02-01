class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        ans = True
        n = len(nums)
        for i in range(n):
            if i!=0:
                if (nums[i]%2==0 and nums[i-1]%2==0) or (nums[i]%2==1 and nums[i-1]%2==1):
                    ans = False
                    return ans
        return ans
