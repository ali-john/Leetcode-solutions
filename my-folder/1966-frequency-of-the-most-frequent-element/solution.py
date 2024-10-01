class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        """
        Greedily image we at ith index we can change all values less than i into nums[i].
        It is only possible when (nums[i])* length (i -> 0) -  sum([0:i])> k.
        In other words, if we have enough room in K to make all previous elements till current index equal to value of
        current index
        """
        nums = sorted(nums)
        n = len(nums)
        max_len = 0

        left = curr =  0
        for right in range(n):
            curr+=nums[right]

            while nums[right]*(right-left+1) - curr > k: # 
                curr-=nums[left]
                left+=1
            max_len = max(max_len,(right-left+1))
        return max_len


        

        
