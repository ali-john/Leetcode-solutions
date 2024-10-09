class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        if n==1:
            if citations[0]==0:
                return 0
            else:
                return 1

        def get_hindex(i)->bool:
            left = 0
            right = n
            while left<right:
                mid = (left+right)//2
                # if citations[mid]==i:
                #     if n-mid>=i:
                #         return True
                #     else:
                #         return False
                if citations[mid] >= i:
                    right = mid
                else:
                    left = mid+1
            if right == n:
                return False
                
            if n-right >=i:
                return True
            else:
                return False

        lo = 0
        hi = 1000

        while lo<=hi:
            mid = (hi+lo)//2
            if get_hindex(mid):
                lo = mid+1
                print(f'true on mid {mid}: lo {lo}, high {hi}')
            else:
                hi = mid - 1
                print(f'false on mid {mid}: lo {lo} , hi {hi}')
        
        return lo-1 

