class Solution:
    def destroyTargets(self, nums: List[int], space: int) -> int:
        n = len(nums)
        nums.sort()

        counts = defaultdict(int)
        max_count = 0
        for i in range(n):
            rem = nums[i]%space
            counts[rem]+=1
        
        max_remainder = max(counts, key = counts.get)
        for num in nums:
            if num%space == max_remainder:
                return num
        return -1
        

            



