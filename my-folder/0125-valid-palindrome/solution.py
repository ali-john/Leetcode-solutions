class Solution:
    def isPalindrome(self, s: str) -> bool:
        n = len(s)
        cleaned_str = []

        for i in range(n):
            if s[i].isalnum():
                cleaned_str.append(s[i].lower())
        
        start_ptr = 0
        end_ptr = len(cleaned_str) - 1

        while start_ptr < end_ptr:
            if cleaned_str[start_ptr] != cleaned_str[end_ptr]:
                return False
            
            start_ptr+=1
            end_ptr-=1
        
        return True
