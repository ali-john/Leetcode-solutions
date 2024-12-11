class Solution:
    def unmarkedSumArray(self, nums: List[int], q: List[List[int]]) -> List[int]:
        m = len(q)
        n = len(nums)

        marked = defaultdict(int)
        heap = []
        total_sum = sum(nums)
        output = []

        for i,num in enumerate(nums):
            pair = (num,i)
            heapq.heappush(heap,pair)
            
        for i, query in enumerate(q):
            index_to_mark = query[0]
            elements_to_mark = query[1]
            temp_sum = 0
            if not index_to_mark in marked:
                temp_sum+=nums[index_to_mark]
                marked[index_to_mark]+=1
            while heap and elements_to_mark:
                pair = heapq.heappop(heap)
                if pair[1] in marked:
                    continue
                else:
                    temp_sum+=pair[0]
                    marked[pair[1]]+=1
                    elements_to_mark-=1
            total_sum-=temp_sum
            output.append(total_sum)
        return output
            
        
