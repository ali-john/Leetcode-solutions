class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        table = defaultdict(int)
        items = sorted(items,key = lambda x: x[0])

        prices = [price for price,beauty in items]

        max_beauty = 0
        for price, beauty in items:
            max_beauty = max(max_beauty, beauty)
            table[price] = max_beauty
        
        # now Binary search over all items to find closed one
        ans = []
        def give_price(val):
            left = 0
            right = len(prices)
            while left<right:
                mid = (left+right)//2
                if prices[mid]<=val:
                    left = mid+1
                else:
                    right = mid
            if prices[left-1]<=val:
                return prices[left-1]
            else:
                return -1
        
        for query in queries:
            price = give_price(query)
            if price==-1:
                ans.append(0)
            else:
                ans.append(table[price])
        
        return ans

        
        

        
