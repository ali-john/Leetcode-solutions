class Solution:
    def minChanges(self, n: int, k: int) -> int:
        if n==k:
            return 0

        n_bin = format(n,'032b')
        k_bin = format(k,'032b')
        count=0
        for i in range(len(n_bin)):
            if n_bin[i]==k_bin[i]:
                continue
            if n_bin[i]=='1' and k_bin[i]=='0':
                count+=1
            if n_bin[i]=='0'and k_bin[i]=='1':
                return -1
        return count


        
