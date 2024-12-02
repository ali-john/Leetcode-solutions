class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        left = 0
        table = defaultdict(int)
        st = set()
        output = -1
        for right in range(n):
            table[s[right]]+=1
            st.add(s[right])

            max_occurance = 0
            max_char = ''
            for char in st:
                if table[char]>max_occurance:
                    max_occurance = table[char]
                    max_char = char
            
            while (right-left+1 - max_occurance > k):
                table[s[left]]-=1
                if table[s[left]]==max_char:
                    max_occurance-=1

                if table[s[left]]==0:
                    del table[s[left]]
                    st.remove(s[left])
                left+=1
            
            output = max(output,(right-left+1))
        return output


            
            


            



