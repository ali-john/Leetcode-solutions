class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        c1 = Counter(words[0])
        vowel_count1 = 0
        for char in ["a","e","i","o","u"]:
            if char in c1:
                vowel_count1+=c1[char]
        
        output = [words[0]]

        for word in words[1:]:
            word_vowel_count = 0
            word_counter = Counter(word)
            for char in ["a","e","i","o","u"]:
                if char in word_counter:
                    word_vowel_count+=word_counter[char]
            if word_vowel_count == vowel_count1:
                word = word[::-1]
            output.append(word)
        return " ".join(output)

