class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        if len(pref)==1:
            return pref
        
        output = []
        output.append(pref[0])
        for i in range(1,len(pref)):
            current = pref[i]
            prev = pref[i-1]
            current = current^prev
            output.append(current)
        return output

