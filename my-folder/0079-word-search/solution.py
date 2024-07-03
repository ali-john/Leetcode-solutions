class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        parents = set()

        def search(index,r,c):
            if index>=len(word):
                return True
            
            if (r<0 or 
            r>=len(board) or 
            c<0 or 
            c>=len(board[0]) or 
            board[r][c]!=word[index] or 
            (r,c) in parents):
                return False
            
            
            parents.add((r,c))

            result= (search(index+1,r,c+1) or 
            search(index+1,r,c-1) or 
            search(index+1,r-1,c) or 
            search(index+1,r+1,c))

            parents.remove((r,c))
            return result
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if search(0,i,j):
                    return True
        return False
            
                
            
        
        
        return res




        
