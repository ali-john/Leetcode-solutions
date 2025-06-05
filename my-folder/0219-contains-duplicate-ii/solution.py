class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        table = defaultdict()
        n = len(nums)

        for i, num in enumerate(nums):
            if num in table:
                dist = i - table[num]
                if dist <= k:
                    return True
            table[num] = i
        return False
