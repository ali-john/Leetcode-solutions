class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        output = True
        for i in range(len(ransomNote)):
            if ransomNote[i] in magazine:
                magazine = magazine.replace(ransomNote[i],'',1)
            else:
                output=False
                break
        return output

            
        
