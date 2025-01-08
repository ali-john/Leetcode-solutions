class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        
        def check(w1,w2):
            if len(w1)>len(w2): return False
            i = 0
            #print(f'w1, {w1}, w2: {w2}')
            for char in w1: # prefix check
                #print(f'forward: char {char}, w2[i]= {w2[i]}')
                if w2[i] == char: 
                    i+=1
                    continue
                else: return False
            i = len(w2) - 1

            for j in range(len(w1)-1,-1,-1):
                #print(f'backward: char {w1[j]}, w2[i]= {w2[i]}')
                if w2[i]==w1[j]:
                    i-=1
                    continue
                else: return False
            return True

        count = 0
        for i in range(len(words)):
            for j in range(i+1,len(words)):
                if check(words[i],words[j]): count+=1
        return count

        


