class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s)<len(p):
            return None
        output = []
        s1 = Counter(p)
        window_count = Counter(s[0:len(p)])

        if s1==window_count:
            output.append(0)
        
        for i in range(len(p),len(s)):
            start_char = s[i-len(p)]
            end_char = s[i]

            window_count[end_char]+=1
            window_count[start_char]-=1

            if window_count[start_char]==0:
                del window_count[start_char]
            
            if s1==window_count:
                output.append(i-len(p)+1)
        return output

        
