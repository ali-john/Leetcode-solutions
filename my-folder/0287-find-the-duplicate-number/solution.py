class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        left, right = 1, n-1

        while left<right:
            mid = (right+left)//2
            cnt = 0
            for i in range(n):
                if nums[i]<=mid:
                    cnt+=1
            if cnt>mid:
                right = mid
            else:
                left = mid+1
        return left
        
        
        



