class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        n = len(nums)
        output = []

        for i in range(n):
            out = 0
            for j in range(n):
                if i == j:
                    continue
                else:
                    if nums[j] < nums[i]:
                        out+=1
            output.append(out)
        return output

