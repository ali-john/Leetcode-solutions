class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        
        total_drank = 0
        empty = 0
        while numBottles:
            total_drank += numBottles
            exchange = numBottles//numExchange
            empty += numBottles - (exchange*numExchange)
            numBottles = exchange
            if empty>=numExchange:
                numBottles += empty//numExchange
                empty = empty%numExchange
        return total_drank


