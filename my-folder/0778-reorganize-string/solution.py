class Solution:
    def reorganizeString(self, s: str) -> str:
        n = len(s)
        table = defaultdict(int)
        max_freq = 0
        letter = ''
        for char in s:
            table[char] +=1
            if table[char] > max_freq:
                max_freq = table[char]
                letter = char
        if max_freq > math.ceil(n / 2): return ""

        ans = ['']*n
        index = 0
        while table[letter]!=0:
            ans[index] = letter
            table[letter]-=1
            index+=2
        
        for char, count in table.items():
            while count > 0:
                if index >= n:
                    index = 1
                ans[index] = char
                index+=2
                count-=1
        return ''.join(ans)

        
        
        
        
        
        
        
        
        
        
        # n = len(s)
        # table = defaultdict(int)
        # max_freq = 0
        # for char in s:
        #     table[char] +=1
        #     max_freq = max(max_freq, table[char])
        
        # if max_freq > math.ceil(n / 2): return ""
        
        # max_heap = []
        # for char , count in table.items():
        #     heapq.heappush(max_heap, (-count, char))
        
        # output = []
        # prev_char , prev_freq = '', 0
        # while max_heap:
        #     count, char = heapq.heappop(max_heap)
        #     output.append(char)

        #     if prev_freq < 0:
        #         heapq.heappush(max_heap, (prev_freq, prev_char))
            
        #     prev_char, prev_freq = char, count + 1
        # return "".join(output)
            

        

