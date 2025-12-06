class Solution:
    def isItPossible(self, word1: str, word2: str) -> bool:

        freq1 = Counter(word1)
        freq2 = Counter(word2)
        sz1 , sz2 = len(freq1) , len(freq2)

        for c1 in ascii_lowercase:
            for c2 in ascii_lowercase:
                if freq1[c1] and freq2[c2]:
                    if c1 == c2:
                        if sz1 == sz2:
                            return True
                    else:
                        cnt1 , cnt2 = sz1, sz2
                        if freq1[c1] == 1: cnt1-=1
                        if freq1[c2] == 0: cnt1+=1
                        if freq2[c2] == 1: cnt2-=1
                        if freq2[c1] == 0: cnt2+=1
                        if cnt1 == cnt2: return True
        return False


       
