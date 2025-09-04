class Solution:
    def partitionString(self, s: str) -> List[str]:
        n = len(s)
        parts = set()
        ans = []
        mapper = defaultdict(int)
        
        current = ""
        for i in range(n):
            current+=s[i]
            if current in parts: continue
            else:
                parts.add(current)
                ans.append(current)
                current = ""
        return ans
        # ans = list(parts)
        # output = [""]*len(ans)
        # for string in ans:
        #     output[mapper[string]] = string
        # return output



