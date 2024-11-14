class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        quantities = sorted(quantities,reverse=True)
        
        def is_possible(val)->bool:
            """
            check if it is possible to distribute quantities with max val quantity
            """
            if val==0:
                return False
            container = 0 # Distribute quantities in containers
            for i in range(len(quantities)):
                quantity = quantities[i]
                to_fill = quantity//val
                container+=to_fill
                if quantity%val!=0:
                    container+=1
                
            if container>n:
                return False
            else:
                return True 

        left = 0
        right = quantities[0]
        last_true = 100000
        while left<=right:
            mid = (left+right)//2
            if is_possible(mid):
                last_true = min(last_true,mid)
                right = mid-1
            else:
                left = mid+1
        return last_true




                        
