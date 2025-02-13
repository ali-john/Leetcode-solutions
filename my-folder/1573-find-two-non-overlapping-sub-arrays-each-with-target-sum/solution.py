class Solution:
    def minSumOfLengths(self, nums: List[int], target: int) -> int:
        n = len(nums)
        windows = [float('inf')]*n

        left = 0
        right = 0
        total = 0
        ans = float('inf')
        minLen = float('inf')
        while right<n:
            total+=nums[right]

            while total>target:
                total-=nums[left]
                left+=1
            if total==target:
                curr = right-left + 1
                if left>0 and windows[left-1]<float('inf'):
                    ans = min(ans,curr+windows[left-1])
                minLen = min(minLen,curr)
                
            windows[right] = minLen
            right+=1
        return -1 if ans==float('inf') else ans
        
        
        
        


