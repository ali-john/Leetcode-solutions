class Solution:
    def numTrees(self, n: int) -> int:
        table = defaultdict(int)
        def backtrack(n,table):
            if table.get(n) is not None:
                return table[n]
            
            if n<=1:
                return 1
            
            count = 0
            for i in range(1,n+1,1):
                left_trees  = backtrack(i-1,table)
                right_trees = backtrack(n-i,table)
                count+= (right_trees*left_trees)
            table[i]=count
            return count
        return backtrack(n,table)

