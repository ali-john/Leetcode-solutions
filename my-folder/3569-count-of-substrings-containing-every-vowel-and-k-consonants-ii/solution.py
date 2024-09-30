class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        vowels = ['a','e','i','o','u']
        n = len(word)


        total = 0
        l = 0
        l_left = 0
        cons_count = 0
        map = defaultdict(int)
        for r in range(n):
            if word[r] in vowels:
                map[word[r]]+=1
            else:
                cons_count+=1

            while cons_count>k and l<r:
                if word[l] in vowels:
                    map[word[l]]-=1

                    if map[word[l]]<=0:
                        del map[word[l]]
                else:
                    cons_count-=1
                
                l+=1
                l_left = l
            
            while cons_count==k and l<r:
                if word[l] in vowels:
                    if map[word[l]]-1>0:
                        map[word[l]]-=1
                        l+=1
                    else:
                        break
                else:
                    break
            if len(map)==5 and cons_count==k:
                total+= (l-l_left+1)
            
        return total


