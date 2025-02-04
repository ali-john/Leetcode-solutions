class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        n = len(nums)

        sub = []

        for num in nums:
            i = bisect_left(sub,num)
            if i==len(sub): sub.append(num)
            else: sub[i] = num

            if len(sub)>=3: return True
        return False
