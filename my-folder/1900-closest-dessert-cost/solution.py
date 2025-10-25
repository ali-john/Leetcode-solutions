class Solution:
    def closestCost(self, base: List[int], topping: List[int], target: int) -> int:
        n = len(base)
        m = len(topping)
        best = None

        def update(cost):
            nonlocal best
            if best is None:
                best = cost
                return 
            best_sofar = abs(target - best)
            updated = abs(target - cost)
            if updated < best_sofar or (best_sofar == updated and cost < best):
                best = cost
            
        def dp(i,curr):
            update(curr)
            if i >=m: return
            dp(i+1, curr) # dont take
            dp(i+1, curr+topping[i])
            dp(i+1, curr+topping[i]*2)

        for b in base:
            dp(0,b)
        return best


        
