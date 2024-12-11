class Solution:
    def minimizeStringValue(self, s: str) -> str:
        count = Counter(s)

        heap = []

        chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm','n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

        for char in chars:
            if char in count:
                heapq.heappush(heap,(count[char],ord(char)))
            else:
                heapq.heappush(heap,(0,ord(char)))

        output = []
        replaced = []
        for i,char in enumerate(s):
            if char=='?':
                replacement = heapq.heappop(heap)
                output.append(chr(replacement[1]))
                replaced.append(chr(replacement[1]))
                heapq.heappush(heap,(replacement[0]+1,replacement[1]))
            else:
                output.append(char)
        replaced.sort()
        ptr = 0
        for i,char in enumerate(s):
            if char =='?':
                output[i] = replaced[ptr]
                ptr+=1
                
        return ''.join(output)
