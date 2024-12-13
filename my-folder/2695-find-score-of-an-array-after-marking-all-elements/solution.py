class Solution:
    def findScore(self, nums: List[int]) -> int:
        n = len(nums)
        score = 0
        heap = []
        marked = defaultdict(int)
        for i,num in enumerate(nums):
            heapq.heappush(heap,(num,i))
        total_marked = 0
       
        while total_marked<n:
            while heap:
                val, index = heapq.heappop(heap)
                if index in marked:
                    continue
                else:
                    score+=val
                    marked[index]+=1
                    total_marked+=1
                    index_right = index+1
                    index_left = index - 1
                    if index_left>=0 and index_left<n:
                        if index_left not in marked:
                            marked[index_left]+=1
                            total_marked+=1
                    if index_right>=0 and index_right<n:
                        if index_right not in marked:
                            marked[index_right]+=1
                            total_marked+=1
                    break
        return score


            


