class Solution:
    def matrixSumQueries(self, n: int, queries: List[List[int]]) -> int:

        rows = set()
        cols = set()

        ans = 0
        for i in range(len(queries) - 1, -1, -1):
            if len(rows) == n or len(cols) == n:
                return ans
            type_, index, val = queries[i]
            if type_ == 0:
                if index in rows: continue
                cols_addition = n - len(cols)
                ans+= (cols_addition*val)
                # for col in range(n):
                #     if col in cols: continue
                #     else:
                #         ans+=val
                rows.add(index)
            else:
                if index in cols: continue
                rows_addition = n - len(rows)
                ans+= (rows_addition*val)
                # for row in range(n):
                #     if row in rows: continue
                #     else:
                #         ans+=val
                cols.add(index)
        return ans



        
                



