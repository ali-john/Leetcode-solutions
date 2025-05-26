class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        n = len(strs)


        ans = []
        first = strs[0]

        for index,char in enumerate(first):
            success = True
            for i in range(1, n):
                if len(strs[i]) > index and strs[i][index] == char:
                    continue
                
                else:
                    success = False
                    break
            if success:
                ans.append(char)
            else:
                break
        
        return "".join(ans) if len(ans) > 0 else ""
            


