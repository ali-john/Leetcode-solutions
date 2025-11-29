class Solution:
    def findIndices(self, nums: List[int], indexDifference: int, valueDifference: int) -> List[int]:
        n = len(nums)
        suffix_min = [0]*n
        suffix_max = [0]*n

        suffix_min[-1] = nums[-1]
        suffix_max[-1] = nums[-1]

        for i in range(n-2, -1, -1):
            suffix_min[i] = min(nums[i], suffix_min[i+1])
            suffix_max[i] = max(nums[i], suffix_max[i+1])
        
        ans = [0,0]
        for i in range(n - indexDifference):
            if abs(nums[i] - suffix_min[i+indexDifference]) >= valueDifference or abs(nums[i] - suffix_max[i+indexDifference]) >= valueDifference:
                ans[0] = i
                for j in range(i+indexDifference, n):
                    if abs(nums[i] - nums[j]) >= valueDifference:
                        ans[1] = j
                        return ans 
        return [-1,-1]
