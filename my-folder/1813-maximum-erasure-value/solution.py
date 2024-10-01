class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        n = len(nums)

        s, left = set(), 0
        curr = 0
        max_count = 0
        for right in range(n):
            curr+=nums[right]

            while left<=right and nums[right] in s:
                curr-= nums[left]
                s.discard(nums[left])
                left+=1
            
            s.add(nums[right])
            max_count = max(max_count,curr)
        return max_count


            



