class Solution:
    def maxJump(self, stones: List[int]) -> int:
        n = len(stones)

        def check(mid):
            for i in range(1, n):
                # one jump
                if stones[i] - stones[i - 1] > mid: return False
                # skip in between
                if i > 1:
                    if stones[i] - stones[i-2] > mid: return False
            return True
        
        lo, hi = 0, 10**9

        while lo <= hi:
            mid = ( lo + hi ) // 2
            if check(mid):
                hi = mid - 1
            else:
                lo = mid + 1
        return lo
        

            









