class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = []
        index = 0
        table = {}
        for i in range(len(strs)):
            string = ''.join(sorted(strs[i]))
            if string in table:
                ind = table[string]
                output[ind].append(strs[i])
            else:
                table[string] = index
                index = index+1
                l = []
                l.append(strs[i])
                output.append(l)
        return output



        






        
