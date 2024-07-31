class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        

        def give_index():
            start = 0
            n = len(letters)
            end = n-1
            target_num = ord(target)
            while start<=end:
                middle = (start+end)//2
                if target_num < ord(letters[middle]):
                    end = middle - 1
                
                else:
                    start = middle+1
            return letters[start%n]
        
        return give_index()






        
