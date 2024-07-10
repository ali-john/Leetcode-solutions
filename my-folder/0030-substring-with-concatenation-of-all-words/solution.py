class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if len(s)<len(words)*len(words[0]):
            return []
    
        words_len = len(words)
        word_len = len(words[0])
        output = []
        words_counter = Counter(words)
        total_len = words_len*word_len
        window_end = 0
        window_start = 0

        for i in range(len(s) - total_len+1):
            substring = s[i:i+total_len]
            segments = [ substring[j:j+word_len] for j in range(0,len(substring),word_len)]
            window_counter = Counter(segments)

            if window_counter == words_counter:
                output.append(i)
        
        return output

            








        
