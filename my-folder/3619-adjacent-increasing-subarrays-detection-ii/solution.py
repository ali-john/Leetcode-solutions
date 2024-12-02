class Solution:
    def maxIncreasingSubarrays(self, nums: List[int]) -> int:
        n = len(nums)

        track = [1]*n
        for i in range(n-2,-1,-1):
            if nums[i]<nums[i+1]:
                track[i] = track[i+1]+1
        print(track)
        def is_possible(k):
            for i in range(n):
                if track[i]>=k:
                    if i+k<n:
                        if track[i+k]>=k:
                            return True
            return False
        
        left = 1
        right = (n//2)+1
        max_ans = -1
        while left<=right:
            mid = (left+right)//2
            if is_possible(mid):
                max_ans = max(max_ans,mid)
                left = mid+1
            else:
                right = mid-1
        return max_ans
            
                
                    
                            
                    
            
            
