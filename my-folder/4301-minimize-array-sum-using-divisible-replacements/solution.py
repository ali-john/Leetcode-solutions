class Solution:
    def minArraySum(self, nums: list[int]) -> int:
        n = len(nums)
        present = set(nums)
        cache = {}

        ans = 0
        for x in nums:
            if x in cache:
                ans+= cache[x]
                continue
            
            d = 1
            smallest = x
            while d**2 <= x:
                if x%d == 0:
                    if d in present:
                        smallest = min(smallest, d)
                    other = x // d
                    if other in present:
                        smallest = min(smallest, other)
                d+=1
            cache[x] = smallest
            ans+=smallest
        return ans
            


