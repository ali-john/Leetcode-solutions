class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        n = len(pattern)
        # count transitions in pattern
        transition_pattern = 0
        for i in range(1,n):
            if pattern[i-1]!=pattern[i]:
                transition_pattern+=1
        ans = []
        # count characters count in pattern
        counter_pattern = Counter(pattern)

        # check if each word has same char count and have same number of transition.
        # IF SO, add it to valid ans
        for word in words:
            word_counter = Counter(word)
            is_valid = True
            for i in range(n):
                count = counter_pattern[pattern[i]]
                if word_counter[word[i]]!=count:
                    is_valid = False
            if is_valid:
                transition_word = 0
                for i in range(1,n):
                    if word[i-1]!=word[i]:
                        transition_word+=1
                if transition_word==transition_pattern:
                    ans.append(word)
        return ans
            


