class Solution:
    def unmarkedSumArray(self, nums: List[int], q: List[List[int]]) -> List[int]:
        n = len(nums)
        output = [0]*len(q)

        heap = []
        for i,num in enumerate(nums):
            pair = (num,i)
            heapq.heappush(heap,pair)
        
        marked = defaultdict(int)
        total_sum = 0
        for i in range(n):
            marked[i] = 0
            total_sum+=nums[i]
        
        for i in range(len(q)):
            index, k = q[i]
            # if not marked, mark it. If already marked, no need to do anything with this index.
            if marked[index] == 0:
                marked[index] = 1 # marked it
                total_sum-=nums[index]
            
            while heap and k:
                val, ind = heapq.heappop(heap)
                # if this is marked, continue to next element
                if marked[ind] == 1: continue
                else:
                    marked[ind] = 1
                    total_sum-=val
                    k-=1
            output[i] = total_sum

        return output

            
                







        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # m = len(q)
        # n = len(nums)

        # marked = defaultdict(int)
        # heap = []
        # total_sum = sum(nums)
        # output = []

        # for i,num in enumerate(nums):
        #     pair = (num,i)
        #     heapq.heappush(heap,pair)
            
        # for i, query in enumerate(q):
        #     index_to_mark = query[0]
        #     elements_to_mark = query[1]
        #     temp_sum = 0
        #     if not index_to_mark in marked:
        #         temp_sum+=nums[index_to_mark]
        #         marked[index_to_mark]+=1
        #     while heap and elements_to_mark:
        #         pair = heapq.heappop(heap)
        #         if pair[1] in marked:
        #             continue
        #         else:
        #             temp_sum+=pair[0]
        #             marked[pair[1]]+=1
        #             elements_to_mark-=1
        #     total_sum-=temp_sum
        #     output.append(total_sum)
        # return output
            
        
