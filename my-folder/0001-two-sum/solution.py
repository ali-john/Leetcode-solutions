class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        output = []
        table = {}

        for i,num in enumerate(nums):
            if table.get(target-num,-1)!=-1:
                output.append(i)
                output.append(table[target-num])
                break
            table[num] = i
            
        return output

        
