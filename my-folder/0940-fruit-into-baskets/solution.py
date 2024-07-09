class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        window_start = 0
        window_end = 0
        output = float("-inf")
        hash_map = {}

        while window_end<len(fruits):
            end_fruit = fruits[window_end]
            hash_map[end_fruit] = hash_map.setdefault(end_fruit,0)+1

            while len(hash_map)>2:
                hash_map[fruits[window_start]]-=1
                if hash_map[fruits[window_start]]==0:
                    del hash_map[fruits[window_start]]
                window_start+=1
            
            output = max(output,(window_end-window_start)+1)
            window_end+=1
        return output







        
