class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        n = len(str1)
        m = len(str2)
        if m>n: # can not be subsequence
            return False
        
        ptr1 = 0
        ptr2 = 0

        while ptr1<n and ptr2<m:
            if str1[ptr1]==str2[ptr2] or chr(((ord(str1[ptr1]) - ord('a') +1)%26)+97) == str2[ptr2]:
                ptr1+=1
                ptr2+=1
                if ptr2>=m:
                    return True
            else:
                ptr1+=1
        return False
        


