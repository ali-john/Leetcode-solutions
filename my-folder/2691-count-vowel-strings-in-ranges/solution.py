class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        n = len(words)
        prefix_arr = [0]*n
        vowels = ['a','e','i','o','u']
        for i in range(n):
            word = words[i]
            if word[0] in vowels and word[-1] in vowels:
                prefix_arr[i] = 1
        
        for i in range(1,n):
            prefix_arr[i] = prefix_arr[i] + prefix_arr[i-1]
        
        output = [0]*len(queries)
        for i, (start,end) in enumerate(queries):
            if start-1 >=0:
                total = prefix_arr[end] - prefix_arr[start-1]
            else:
                total = prefix_arr[end]
            output[i] = total
        return output
