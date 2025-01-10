class Solution:
    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:
        def count(word):
            ans = [0]*26
            for char in word:
                ans[ord(char) - ord('a')]+=1
            return ans
        
        output = []
        bmax = [0]*26

        for b in B:
            for i, c in enumerate(count(b)):
                bmax[i] = max(c,bmax[i])
        
        for a in A:
            if all(x>=y for x,y in zip(count(a),bmax)):
                output.append(a)
        return output
            
