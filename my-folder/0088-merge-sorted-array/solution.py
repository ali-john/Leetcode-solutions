class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # two pointers solution

        temp = nums1[:m]
        ptr1  = 0
        ptr2 = 0
        i = 0

        while ptr1 < m and ptr2 < n:
            if temp[ptr1] <= nums2[ptr2]:
                nums1[i] = temp[ptr1]
                ptr1+=1
            else:
                nums1[i] = nums2[ptr2]
                ptr2+=1
            i+=1
        
        while ptr1 < m:
            nums1[i] = temp[ptr1]
            ptr1+=1
            i+=1
        
        while ptr2 < n:
            nums1[i] = nums2[ptr2]
            ptr2+=1
            i+=1
        
        

        



        # heap solution 
        # heap = []
        # for i in range(m):
        #     heapq.heappush(heap,nums1[i])
        
        # for i in range(n):
        #     heapq.heappush(heap,nums2[i])
        
        # i = 0
        # while heap:
        #     element = heapq.heappop(heap)
        #     nums1[i] = element
        #     i+=1


        


        
