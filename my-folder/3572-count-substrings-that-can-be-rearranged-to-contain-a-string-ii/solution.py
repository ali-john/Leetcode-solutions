class Solution:
    def validSubstringCount(self, word1: str, word2: str) -> int:
        n = len(word1)
        k = len(word2)
        word2_c= Counter(word2)
        word1_c = Counter()
        total = 0
        start = 0

        for i in range(n):
            curr = word1[i]

            if word2_c[curr]>0:
                if word1_c[curr]<word2_c[curr]:
                    k-=1
            
            word1_c[curr]+=1

            while k==0:
                total+=n-i
                pre = word1[start]
                word1_c[pre]-=1
                if word2_c[pre]>0 and word1_c[pre]<word2_c[pre]:
                    k+=1
                start+=1
        return total
