class Solution:
    def sumOfEncryptedInt(self, nums: List[int]) -> int:

        output = []
        n = len(nums)
        for number in nums:
            digits = [int(digit) for digit in str(number)]
            digits.sort()
            max_digit = digits[-1]
            output_str = []
            for i in range(len(str(number))):
                output_str.append(str(max_digit))
            output.append(int(''.join(output_str)))
        return sum(output)
            
            
