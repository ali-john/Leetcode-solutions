class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        for char in paragraph:
            if char in "!?',;.":
                paragraph = paragraph.replace(char," ")
        paragraph_letters = paragraph.split()
        lower_letters = [] 
        for letter in paragraph_letters:
            lower_letters.append(letter.lower())
        
        letters_counter = Counter(lower_letters)
        ans = ''
        freq = float('-inf')
        #print(letters_counter)
        for letter,f in letters_counter.items():
            if f>freq:
                if letter not in banned:
                    ans = letter
                    freq = f
        return ans


