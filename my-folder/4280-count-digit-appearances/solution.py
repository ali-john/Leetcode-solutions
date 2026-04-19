class Solution:
    def countDigitOccurrences(self, nums: list[int], digit: int) -> int:
        count = 0
        for element in nums:
            while element > 0:
                if (digit == element%10):
                    count+=1
                element//=10
        return count
        # for i in range(len(nums)):
        #     element = str(nums[i])
        #     for d in element:
        #         if int(d) == digit:
        #             count+=1
        # return count

        
