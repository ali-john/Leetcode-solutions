class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        def backtrack(nums):
            result = []
            if len(nums)==1:
                return [nums[:]]
            
            for i in range(len(nums)):
                num = nums.pop(0)
                perms = backtrack(nums)

                for perm in perms:
                    perm.append(num)
                result.extend(perms)
                nums.append(num)
            return result

        return backtrack(nums)
    


        
