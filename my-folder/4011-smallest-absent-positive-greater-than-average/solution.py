class Solution:
    def smallestAbsent(self, nums: List[int]) -> int:
        n = len(nums)
        table = Counter(nums)

        def find_num(start):
            for i in range(start,200):
                if i not in table:
                    return i
        
        avg = sum(nums)//n
        start = avg + 1
        ans = find_num(start) if start > 0 else find_num(1)
        return ans
        
