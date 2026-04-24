class Solution:
    def expressiveWords(self, S: str, words: List[str]) -> int:

        # compress a word into a letter sequence and corresponding counts
        def compress(word):
            letters = []
            counts = []
            for l in word:
                if not letters or l != letters[-1]:
                    letters.append(l)
                    counts.append(1)
                else:
                    counts[-1] += 1
                    
            return letters, counts
        
        # check if a word is stretchy by comparing to compressed S
        def is_stretchy(w):
            
            # S_letters, S_counts are the output of compress(S)
            nonlocal S_letters, S_counts
            
            w_letters, w_counts = compress(w)
            
            if w_letters != S_letters:
                return False
            
            for i in range(len(S_counts)):
                if S_counts[i] < 3 and S_counts[i] != w_counts[i]:
                    return False
                if S_counts[i] >= 3 and S_counts[i] < w_counts[i]:
                    return False
                    
            return True

        # main body
        S_letters, S_counts = compress(S)
        res = 0
        for w in words:
            if is_stretchy(w):
                res += 1
        
        return res
