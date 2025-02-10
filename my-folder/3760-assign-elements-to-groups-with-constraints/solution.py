class Solution:
    def assignElements(self, groups: List[int], elements: List[int]) -> List[int]:
        n = len(groups)
        ans = [-1]*n

        elements_index = defaultdict(int)
        for i,num in enumerate(elements):
            if num not in elements_index:
                elements_index[num] = i
        
        for i,num in enumerate(groups):
            prev_index = float('inf')

            for j in range(1,int(num**0.5)+1):
                if num%j == 0:
                    if j in elements_index: prev_index = min(prev_index,elements_index[j])
                    if (num//j) in elements_index:
                        prev_index = min(prev_index,elements_index[num//j])
            
            if prev_index!= float('inf'):
                ans[i] = prev_index
        
        return ans


