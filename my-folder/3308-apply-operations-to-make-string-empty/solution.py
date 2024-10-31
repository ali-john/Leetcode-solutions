class Solution:
    def lastNonEmptyString(self, s: str) -> str:
        table = defaultdict(list)

        for i,char in enumerate(s):
            table[char].append(i)

        max_len = 0
        for key,val in table.items():
            max_len = max(max_len,len(val))
        if max_len==1: # can not remove anything
            return s

        else:
            keys = table.keys()
            to_delete = []
            for key in keys:
                if len(table[key])<max_len:
                    to_delete.append(key)
                else:
                    table[key] = table[key][-1]
            for key in to_delete:
                del table[key]
        #print(table)
        
            
        
        
        ans = []
        
        while len(table.keys())>0:
            min_index,min_char = float("inf"), ''
            keys = table.keys()
            for char in keys:
                if table[char]<min_index:
                    min_char = char
                    min_index = table[char]
            ans.append(min_char)
            #print(ans)
            del table[min_char]
                    
        return ''.join(ans)
        #return "s"
        
