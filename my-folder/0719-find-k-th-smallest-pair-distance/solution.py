class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        def count_pairs(val):
            count = 0
            i = 0
            for j in range(n):
                while nums[j]-nums[i]>val:
                    i+=1
                count+= j-i
            return count

        left = 0
        right = nums[-1] - nums[0]

        while left<right:
            mid = (left+right)//2
            if count_pairs(mid)>=k:
                right = mid
            else:
                left = mid+1
        return left
