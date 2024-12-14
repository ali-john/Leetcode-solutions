class Solution:
    def sumIndicesWithKSetBits(self, nums: List[int], k: int) -> int:


        ans = 0
        n = len(nums)
        for i in range(n):
            binary = bin(i)[2:]
            ones = 0
            for j in range(len(binary)):
                if binary[j]=='1':
                    ones+=1
            if ones==k:
                ans+=nums[i]
        return ans
                    
