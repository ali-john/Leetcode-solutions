class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        output = [[]]
        n = len(nums)
        def backtrack(index):
            if index==n:
                return
            
            for i in range(len(output)):
                new_s = output[i][:]
                new_s.append(nums[index])
                output.append(new_s[:])
            
            backtrack(index=index+1)
            return

        backtrack(index = 0)
        return output

                



