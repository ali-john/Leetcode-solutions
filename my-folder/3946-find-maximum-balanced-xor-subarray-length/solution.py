class Solution:
    def maxBalancedSubarray(self, nums: List[int]) -> int:
        n = len(nums)

        xor = 0
        even = 0
        odd = 0

        seen = {(0,0):-1}
        best = 0

        for i, num in enumerate(nums):
            xor^=num
            if num%2 == 0:
                even+=1
            else:
                odd+=1

            key = (xor, even - odd)
            if key in seen:
                best = max(best, i - seen[key])
            else:
                seen[key] = i
        return best


     
        

