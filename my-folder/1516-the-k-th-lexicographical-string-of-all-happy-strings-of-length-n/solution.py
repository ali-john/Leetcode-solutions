class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        
        all_str = []

        def generate(string):
            if len(string) == n:
                all_str.append(string)
                return
            
            for char in ['a','b','c']:
                if len(string) > 0 and char == string[-1]: continue
                generate(string+char)

        generate("")
        if k> len(all_str): return ""
        else:
            all_str.sort()
            return all_str[k-1]


