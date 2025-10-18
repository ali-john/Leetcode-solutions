class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        ans, current = 2, 2
        for i in range(2,n):
            if nums[i] == (nums[i-1] + nums[i-2]):
                current+=1
            else:
                current = 2
            ans = max(ans, current)
        return ans







        # n = len(nums)
        # cond = [False]*n
        # for i in range(2,n):
        #     prev = nums[i-1] + nums[i-2]
        #     if prev == nums[i]:
        #         cond[i] = True
        
        # # check longest Trues
        # maxi = 0
        # i = 2
        # while i < n:
        #     current = 0
        #     while i < n and cond[i]:
        #         current+=1
        #         i+=1
        #     maxi = max(maxi, current)
        #     i+=1
        # return maxi + 2

            





