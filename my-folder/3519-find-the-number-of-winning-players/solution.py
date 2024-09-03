class Solution:
    def winningPlayerCount(self, n: int, pick: List[List[int]]) -> int:
        table = defaultdict(list[list])

        for player,color in pick:
            table[player].append(color)
        output = []
        for key,val in table.items():
            if len(val)>0:
                vals = sorted(table[key])
                max_count = 1
                current_count = 1
                j = vals[0]
                for i in range(1,len(vals)):
                    if vals[i]==j:
                        current_count+=1
                    else:
                        j = vals[i]
                        current_count = 1
                    
                    max_count = max(max_count,current_count)
                if max_count>key:
                    output.append(key)
        #print(output)     
        return len(output) if len(output)>0 else 0
