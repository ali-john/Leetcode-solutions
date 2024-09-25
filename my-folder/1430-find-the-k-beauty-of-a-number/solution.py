class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        nn = str(num)

        total = 0
        for i in range(len(nn)-k+1):
            sub = nn[i:i+k]
            intt = int(sub)
            if intt!=0:
                if num%intt==0:
                    total+=1
        return total

