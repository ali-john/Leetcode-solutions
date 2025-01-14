class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        n = len(A)
        output = [0]*n
        table = defaultdict(int)
        for i in range(1,n+1):
            table[i] = 0
        
        for i in range(n):
            table[A[i]]+=1
            table[B[i]]+=1
            count = 0
            for j in range(1,n+1):
                if table[j]==2:
                    count+=1
            output[i] = count
        return output
            



