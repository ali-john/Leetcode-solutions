class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(t)== len(s):
            output = True
            n = len(t)
            for i in range(n):
                letter = t[i]
                count = t.count(letter)
                if letter in s:
                    s_count = s.count(letter)
                    if s_count != count:
                        output = False
                        return output
                else:
                    output = False
                    return output
            return output

    
        else:
            return False
        

        
