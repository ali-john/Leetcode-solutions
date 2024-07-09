class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        window_start = 0
        window_end = 0
        hash_table= {}
        output = float("-inf")
        if len(s)==0:
            return 0
        while window_end<len(s):
            present_chr = s[window_end]

            if present_chr in hash_table:
                window_start = max(window_start,hash_table[present_chr]+1)
            
            hash_table[present_chr] = window_end
            output = max(output, (window_end-window_start)+1)
            window_end+=1
        return output

           

            

