class Solution:
    def findValidPair(self, s: str) -> str:
        n = len(s)
        counter = defaultdict(int)
        for char in s:
            counter[int(char)]+=1

        ans = []

        for i,char in enumerate(s):
            char = int(char)
            if i+1<n:
                next_char = int(s[i+1])
                if next_char!=char:
                    if counter[char]==char and next_char==counter[next_char]:
                        ans.append(str(char))
                        ans.append(str(next_char))
                        return ''.join(ans)
            
        return ''
                
