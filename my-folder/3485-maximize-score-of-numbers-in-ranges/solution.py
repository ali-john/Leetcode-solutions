class Solution:
    def maxPossibleScore(self, start: List[int], d: int) -> int:
        n = len(start)
        start = sorted(start)

        def possible(gap):
            nums = start[:]

            for i in range(1,n):
                curr = nums[i - 1] + gap
                if nums[i] > curr:
                    continue
                if nums[i] <= curr <= nums[i] + d:
                    nums[i] = curr
                else:
                    return False
            return True

        left, right = 0, 10**19
        while left <= right:
            gap = (left+right) // 2
            #print(f'gap = {gap}')
            if possible(gap):
                left = gap + 1
            else:
                right = gap - 1
        return left - 1




        
