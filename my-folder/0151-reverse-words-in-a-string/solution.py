class Solution:
    def reverseWords(self, s: str) -> str:

        def split() -> list:
            n = len(s)
            out = []

            i = 0
            while i < n:
                if s[i]!=' ':
                    temp = s[i]
                    for j in range(i+1, n):
                        if s[j]!=' ':
                            temp+=s[j]
                            i = j
                        else:
                            i = j
                            break
                    out.append(temp)
                i+=1
            return out

        
        test = split()
        ans = []
        for i in reversed(range(len(test))):
            if len(test[i]) > 0:
                ans.append(test[i])
                ans.append(' ')

        return "".join(ans[:-1])
