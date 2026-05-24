class Solution:
    def limitOccurrences(self, nums: list[int], k: int) -> list[int]:
        n = len(nums)
        table = Counter(nums)
        processed = set()
        ans = []
        for num in nums:
            if num not in processed:
                processed.add(num)
                if table[num] >=k:
                    ans.extend([num]*k)
                else:
                    ans.extend([num]*table[num])
        return ans
