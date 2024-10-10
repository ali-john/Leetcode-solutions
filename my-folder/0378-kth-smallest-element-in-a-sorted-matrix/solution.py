class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        
        n = len(matrix)

        def count_less_or_equal(val):
            cnt = 0
            c = n-1
            for r in range(n):
                while c>=0 and matrix[r][c]>val:
                    c-=1
                cnt+= (c+1)
            return cnt

        
        left = matrix[0][0]
        right = matrix[-1][-1]
        ans = -1
        while left<=right:
            mid = (left+right)//2
            if count_less_or_equal(mid)>=k:  
                right = mid-1
                ans = mid
            else:
                left = mid+1
        return ans
        

