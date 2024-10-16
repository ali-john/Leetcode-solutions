class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        element_sum = sum(nums)

        digit_sum = 0
        for i in range(len(nums)):
            integer = nums[i]
            string = str(integer)
            for char in string:
                digit_sum+=int(char)
        
        return abs(element_sum-digit_sum)
