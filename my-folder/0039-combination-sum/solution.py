class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        output = []
        def backtrack(i, curr,total):
            if total == target:
                output.append(curr[:])
                return 
            
            if total>target or i>=len(candidates):
                return 
            
            curr.append(candidates[i])
            backtrack(i,curr,total+candidates[i])
            curr.pop()
            backtrack(i+1,curr,total)
    
        backtrack(0,[],0)
        return output


            
            


            
                


        
