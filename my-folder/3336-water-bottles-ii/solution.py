class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:

        empty = 0
        bottles = numBottles
        exchange = numExchange
        drank = 0

        while bottles:
            drank+=bottles
            empty+=bottles
            bottles = 0
            # now exchange bottles:
            while (empty - exchange) >=0:
                bottles+=1
                empty = empty-exchange
                exchange+=1
        return drank
            
            
