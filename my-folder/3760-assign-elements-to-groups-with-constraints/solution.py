class Solution:
    def assignElements(self, groups: List[int], elements: List[int]) -> List[int]:

        n = len(groups)
        output = [-1]*n

        table = defaultdict(int)

        for i, num in enumerate(elements): # map each index
            if num not in table:
                table[num] = i
        
        for i, num in enumerate(groups):
            index = float('inf')
            for divisor in range(1,int(num**0.5)+1):
                if num%divisor == 0:
                    if divisor in table:
                        index = min(index, table[divisor])
                    if (num//divisor) in table:
                        index = min(index, table[num//divisor])
            if index != float('inf'):
                output[i] = index
        return output













        # n = len(groups)
        # ans = [-1]*n
        # index_map = defaultdict(int)
        # for i,num in enumerate(elements):
        #     if num not in index_map:
        #         index_map[num] = i
        
        # for i,num in enumerate(groups):
        #     divisor = 1
        #     index = float("inf")
        #     for divisor in range(1, int(num**0.5)+1):
        #         if num%divisor==0:
        #             if divisor in index_map:
        #                 index = min(index,index_map[divisor])
        #             if (num//divisor) in index_map:
        #                 index = min(index,index_map[num//divisor])
        #     if index!=float("inf"):
        #         ans[i] = index
        # return ans
        
