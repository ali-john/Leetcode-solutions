
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        table = defaultdict(int)
        for i in range(len(s)-9):
            seq = s[i:i+10]
            table[seq]+=1
        
        output = []
        for key,val in table.items():
            if val>1:
                output.append(key)
        return output
        
