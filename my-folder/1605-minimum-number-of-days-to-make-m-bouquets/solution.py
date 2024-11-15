class Solution:
    def minDays(self, nums: List[int], m: int, k: int) -> int:
        n = len(nums)
        if m*k>n:
            return -1
        

        def is_possible(val):
            """
            returns True if possible to make bucket with val number of days else False
            """
            buckets = 0
            i = 0
            window = 0
            while i<n:
                if nums[i]<=val:
                    window+=1
                else:
                    window = 0
                
                if window==k:
                    buckets+=1
                    window = 0
                i+=1
            if buckets>=m:
                return True
            else: return False
        
        # Binary search over ans to get minimum number
        left = min(nums)
        right = max(nums)
        min_days = 1000000000
        while left<=right:
            mid = (left+right)//2

            if is_possible(mid):
                min_days = min(min_days,mid)
                right = mid-1
            else:
                left = mid+1
        return min_days


