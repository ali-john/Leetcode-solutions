class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        n = len(arr)
        prefix = [0]*n
        prefix[0] = arr[0]

        for i in range(1,n):
            prefix[i] = prefix[i-1]^arr[i]
        
        q = len(queries)
        answer = [0]*q
        for i in range(q):
            start, end = queries[i]
            if start>0:
                ans = prefix[end]^prefix[start-1]
            else:
                ans = prefix[end]^0
            
            answer[i] = ans
        return answer
            
