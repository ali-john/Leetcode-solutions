class Solution:
    def maxScore(self, nums: List[int], x: int) -> int:
        n = len(nums)

        memo = {}
        def dp(i, isEven):
            if (i,isEven) in memo: return memo[(i,isEven)]
            if i>=n: return 0
            take, dont_take = 0, 0
            if isEven:
                if nums[i] % 2 ==0:
                    take = nums[i] + dp(i+1, True)
                else:
                    take = nums[i] - x + dp(i+1, False)
            else:
                if nums[i] % 2 == 0:
                    take = nums[i] - x + dp(i+1, True)
                else:
                    take = nums[i] + dp(i+1, False)
            dont_take = dp(i+1, isEven)
            memo[(i,isEven)] = max(take, dont_take)
            return memo[(i,isEven)]
        
        even = dp(0,nums[0]%2 == 0)
        return even
        #odd = dp(0,False)
        #return max(even, odd)



