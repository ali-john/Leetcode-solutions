class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        output = [[]]
        nums = sorted(nums)
        n = len(nums)
        def backtrack(index,created):
            if index==n:
                return
            prev_len = len(output)
            
            if index>0 and nums[index]==nums[index-1]:
                to_add = copy.deepcopy(output[-1:-created-1:-1])
                for sub in to_add:
                    sub.append(nums[index])
                    output.append(sub[:])
                
            else:
                for i in range(len(output)):
                    sub = output[i][:]
                    sub.append(nums[index])
                    output.append(sub[:])
            
            created = len(output)-prev_len
            backtrack(index+1,created)
        backtrack(0,0)
        return output
