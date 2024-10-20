class Solution:
    def numberOfSubstrings(self, s: str, k: int) -> int:
        def is_valid(table):
            for key,val in table.items():
                if val>=k:
                    return True
            return False

        n = len(s)
        table = defaultdict(int)
        left = 0
        l_left = 0
        total = 0

        for right in range(n):
            table[s[right]]+=1
            while is_valid(table):
                total+=(n-right)
                table[s[left]] -= 1
                if table[s[left]] == 0:
                    del table[s[left]]
                left += 1  
        return total
            




