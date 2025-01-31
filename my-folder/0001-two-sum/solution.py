class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        output = []
        table = defaultdict(int)
        
        for i,num in enumerate(nums):
            if target - num in table:
                output.append(i)
                output.append(table[target - num])
            table[num] = i
        return output
