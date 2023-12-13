class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        out = []
        for i in range(len(nums)):
            p = nums[i]
            for j in range(i+1,len(nums)):
                q = nums[j]
                if (p+q) == target:
                    out.append(i)
                    out.append(j)
        return out

        