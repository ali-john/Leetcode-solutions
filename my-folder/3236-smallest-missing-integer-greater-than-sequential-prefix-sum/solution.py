class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        n = len(nums)
        counter = Counter(nums)

        total = nums[0]
        for i in range(1,n):
            if nums[i]==nums[i-1]+1:
                total+=nums[i]
            else:
                break
        
        while total in counter:
            total+=1
        return total

