class Solution:
    def minimumSize(self, nums: List[int], operations: int) -> int:
        n = len(nums)

        def check(val,op):
            for i,num in enumerate(nums):
                op-=(num//val)
                if num%val==0:
                    op+=1
            return op>=0 

        


        last_true = float('inf')
        left = 1
        right = 10000000000

        while left<=right:
            mid = (left+right)//2
            if check(mid,operations):
                last_true = min(last_true,mid)
                right = mid-1
            else:
                left = mid+1
        return last_true

