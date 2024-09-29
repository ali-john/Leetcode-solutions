class Solution:
    def kthCharacter(self, k: int) -> str:
        def change(char):
            return ''.join(chr(((ord(c) + 1) - 97) % 26 + 97) for c in char)
            
        
        word = "a"
        n = math.ceil(k**0.5)
        while len(word)<k:
            word+=change(word)
        return word[k-1]



