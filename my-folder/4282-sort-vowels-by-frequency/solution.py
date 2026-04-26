class Solution:
    def sortVowels(self, s: str) -> str:
        n = len(s)
        vowels = ['a', 'e', 'i', 'o', 'u']
        vowels_dict = defaultdict() # list of (count, occurance_index)
        for i, char in enumerate(s):
            if char in vowels:
                if char in vowels_dict:
                    vowels_dict[char][0]+=1
                else:
                    vowels_dict[char] = [1, i]
        vowels_sorted = []
        for key,value in vowels_dict.items():
            value.append(key)
            vowels_sorted.append(value)
        vowels_sorted = sorted(vowels_sorted, key = lambda x: (-x[0], x[1]))
        output = []
        vowels_ptr = 0
        for i in range(n):
            if s[i] in vowels:
                output.append(vowels_sorted[vowels_ptr][2])
                vowels_sorted[vowels_ptr][0]-=1
                if vowels_sorted[vowels_ptr][0] == 0:
                    vowels_ptr+=1
            else:
                output.append(s[i])
        return ''.join(output)





