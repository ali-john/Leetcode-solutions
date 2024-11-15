class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        nums = [start]
        for i in range(1,n):
            nums.append((start)+(2*i))
        

        ans = nums[0]
        for i in range(1,n):
            ans^=nums[i]
        return ans
