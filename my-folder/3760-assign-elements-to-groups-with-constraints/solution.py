class Solution:
    def assignElements(self, groups: List[int], elements: List[int]) -> List[int]:

        n = len(groups)
        table = defaultdict(int)
        for i , num in enumerate(elements):
            if num not in table:
                table[num] = i
        
        ans = []
        for i,num in enumerate(groups):
            possible = len(elements) 
            for divisor in range(1, int(num**0.5) + 1):
                if num% divisor == 0:
                    if divisor in table:
                        possible = min(possible, table[divisor])
                    if ( num // divisor) in table:
                        possible = min(possible, table[num//divisor])

            if possible != len(elements):
                ans.append(possible)
            else:
                ans.append(-1)
        return ans

