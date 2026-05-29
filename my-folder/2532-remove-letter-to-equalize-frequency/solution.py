class Solution:
    def equalFrequency(self, word: str) -> bool:
        def check(table):
            first = next(iter(table.values()))
            return all(value == first for value in table.values())
    
        n = len(word)
        for char in word:
            temp_counter = Counter(word)
            temp_counter[char]-=1
            if temp_counter[char] == 0: del temp_counter[char]
            #print(f'char: {char}, temp_counter:{temp_counter}')
            if check(temp_counter):
                return True
        return False
