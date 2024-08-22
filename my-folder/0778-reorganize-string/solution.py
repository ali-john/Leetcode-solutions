class Solution:
    def reorganizeString(self, s: str) -> str:
        n = len(s)
        max_count = 0
        table = defaultdict(int)
        max_heap = []

        for char in s:
            table[char]+=1
            if table.get(char)>max_count:
                max_count=table.get(char) # max count of any char
        if max_count> math.ceil(n/2):
            return ""
        
        for key,val in table.items():
            heapq.heappush(max_heap, (-val,key))
        
        output = []
        prev_char, prev_freq = '', 0
        while max_heap:
            freq,char = heapq.heappop(max_heap)
            output.append(char)

            if prev_freq<0:
                heapq.heappush(max_heap,(prev_freq, prev_char))
            
            prev_freq, prev_char = freq+1, char

        return "".join(output)

            


