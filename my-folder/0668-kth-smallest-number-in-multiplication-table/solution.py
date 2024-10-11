class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        # since rows and columns will be sorted, use BS
        def count_small(val):
            j = n
            cnt = 0
            for i in range(1,m+1):
                while j>0 and (i*j)>val:
                    j-=1
                cnt+=j
            return cnt


        left = 1
        right = m*n
        ans = 0
        while left<=right:
            mid = (left+right)//2
            if count_small(mid)>=k:
                right = mid-1
                ans = mid
            else:
                left = mid+1
        return ans


