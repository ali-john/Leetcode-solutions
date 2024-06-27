class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        numbers = [num for num in range(1,n+1)]
        if n==1:
            return [[1]]
        output = []

        def backtrack(index,combination):
            
            
            if len(combination) == k:
                output.append(combination[:])
                return
                
            for i in range(index,n+1):
                combination.append(i)
                backtrack(i+1,combination)
                combination.pop()
                    
        backtrack(1,[])
        return output
