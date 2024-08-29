class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        n = len(s)
        output = []
        def backtrack(i,permutation):
            if len(permutation)==n:
                output.append(permutation[:])
                return 
            if i>n:
                return 

            char = s[i]
            if char.isdigit():
                permutation.append(char)
                backtrack(i+1,permutation)
                permutation.pop()
            else:
                upper = char.upper()
                lower = char.lower()
                permutation.append(upper)
                backtrack(i+1,permutation)
                permutation.pop()
                permutation.append(lower)
                backtrack(i+1,permutation)
                permutation.pop()
        
        backtrack(0,[])
        list_final = []
        for sub in output:
            list_final.append("".join(char for char in sub))
        return list_final




            
            
        



                
            


