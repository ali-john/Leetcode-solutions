class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        wordList = set(wordList)
        q = []
        charSet = set(w for word in wordList for w in word)
        q.append((beginWord,1))
        visited = set()
        visited.add(beginWord)
        while q:
            word,level = q.pop(0)
            for i in range(len(word)):
                for letter in charSet:
                    new_word = word[:i]+letter+word[i+1:]
                    if new_word not in visited and new_word in wordList and new_word!=word:
                        if new_word == endWord:
                            return level+1
                        q.append((new_word,level+1))
                        visited.add(new_word)
                        wordList.remove(new_word)
        return 0
            
                    



        
