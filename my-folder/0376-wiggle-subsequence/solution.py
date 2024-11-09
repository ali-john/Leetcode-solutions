class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        n = len(nums)
        @cache
        def solve(i,prev,sign):
            if i>=n:
                return 0
            
            diff = nums[i] - prev
            if diff==0:
                solve(i+1,prev,sign)

            if (sign==-1 and diff>0) or (sign==1 and diff<0):
                new_sign = -sign
                return max(solve(i+1,prev,sign), 1+solve(i+1,nums[i],new_sign))

            else:
                return solve(i + 1, prev, sign)

        return max(1 + solve(1, nums[0], 1), 1 + solve(1, nums[0], -1))
        

            

