class Solution:
    def sumDigitDifferences(self, nums: List[int]) -> int:
        n = len(nums)
        digits_len = len(str(nums[0]))

        ans = 0
        for i in range(digits_len):
            counter = defaultdict(int)
            # get all digits at ith position in all numbers
            for num in nums:
                digits = [ int(m) for m in str(num)]
                counter[digits[i]]+=1
            # calculate contributions:
            for i in range(0,10,1):
                if i in counter:
                    for j in range(i+1,10,1):
                        if j in counter:
                            contrib = counter[i] * counter[j]
                            ans+=contrib
        return ans


        
        return ans



