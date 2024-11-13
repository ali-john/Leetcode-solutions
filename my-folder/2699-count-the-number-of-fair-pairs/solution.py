class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums = sorted(nums)
        n = len(nums)
        def count_pairs(target):
            left = 0
            right = n-1
            count = 0
            while left<right:
                mid = (left+right)//2
                if nums[left]+nums[right]<=target:
                    count+=(right-left)
                    left+=1
                else:
                    right-=1
            return count

        return count_pairs(upper) - count_pairs(lower-1)
