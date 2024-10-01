class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        n = len(nums)
        target = sum(nums)-x
        if target==0:
            return n
        
        left , max_len, curr = 0, 0 , 0 

        for right in range(n):
            curr+= nums[right]

            while left<=right and curr>target:
                curr-=nums[left]
                left+=1
            
            if curr==target:
                max_len = max(max_len,(right-left+1))
                
        return n-max_len if max_len else -1


