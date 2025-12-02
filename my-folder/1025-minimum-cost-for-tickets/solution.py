class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        n = len(days)
        travel_days = set(days)
        last_day = days[-1]

        @cache
        def dp(currDay):
            if currDay > last_day:
                return 0
            
            if currDay not in travel_days:
                return dp(currDay+1)
            
            one_day = costs[0] + dp(currDay + 1)
            seven_day = costs[1] + dp(currDay + 7)
            thirty_day = costs[2] + dp(currDay + 30)

            return min(one_day, seven_day, thirty_day)
        
        return dp(1)



       
