class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        n = len(strs)
        table = defaultdict()
        output = []

        for st in strs:
            m = "".join(sorted(st))
            if m in table:
                output[table[m]].append(st)
            else:
                table[m] = len(output)
                output.append([st])
        
        return output


        
        
