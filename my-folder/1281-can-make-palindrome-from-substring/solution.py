class Solution:
    def canMakePaliQueries(self, s: str, queries: List[List[int]]) -> List[bool]:

        n = len(s)
        count = [[0]*n for _ in range(26)]

        for i in range(n):
            count[ord(s[i])-ord('a')][i]+=1
        # find prefix sum of count:
        for i in range(26):
            l = count[i]
            for j in range(1,n):
                l[j] = l[j]+l[j-1]
        
        # process queris:
        q = len(queries)
        answer = [False]*q
        for i in range(q):
            start,end,rep = queries[i]
            odd_count = 0 
            for j in range(26):
                l = count[j]
                char_count = l[end] - (l[start-1] if start>0 else 0)
                if char_count%2!=0: # odd char
                    odd_count+=1
            if (odd_count)//2 <=rep:
                answer[i] = True
        
        return answer


