class Solution:
    def maximumValue(self, strs: List[str]) -> int:
        max_val = 0
        for string in strs:
            numeric = False
            alpha = False
            for char in string:
                if char.isalpha():
                    alpha = True
                else:
                    numeric = True
            if numeric and not alpha:
                max_val = max(max_val,int(string))
            elif  alpha:
                max_val = max(max_val,len(string))
        return max_val
