class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        # The idea is to brute force all 32 bits from lsb and check if unsetting any bit makes the condition nums[i]|nums[i]+1 == nums[i] True. This will be the smallest answer because we are traversing from LSB
        n = len(nums)
        output = [-1]*n

        for i in range(n):
            max_num = bin(nums[i])[2:]
            print(max_num)
            for j in range(len(max_num)-1,-1,-1):
                if list(max_num)[j]=='1':
                    new_num = list(max_num)
                    new_num[j] = '0'
                    new_num = ''.join(new_num)
                    new_num = int(new_num,2)
                    if (new_num| new_num+1) == nums[i]:
                        output[i] = new_num

        return output
