import heapq as h
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:

        heap = []
        visited = set()
        output = []
        h.heappush(heap,(nums1[0]+nums2[0],0,0))
        visited.add((0,0))

        while k and heap:
            _, i, j = h.heappop(heap)
            output.append([nums1[i],nums2[j]])

            while i+1<len(nums1) and (i+1,j) not in visited:
                h.heappush(heap,(nums1[i+1]+nums2[j],i+1,j))
                visited.add((i+1,j))
            
            while j+1<len(nums2) and (i,j+1) not in visited:
                h.heappush(heap,(nums1[i]+nums2[j+1],i,j+1))
                visited.add((i,j+1))
            
            k-=1
        return output
        

        



        

        
