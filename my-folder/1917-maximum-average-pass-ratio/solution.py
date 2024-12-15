class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extra: int) -> float:
        n = len(classes)
        heap  = []

        for i in range(n):
            item = classes[i]
            passes = classes[i][0]
            total_students = classes[i][1]
            gain = (passes+1) / (total_students+1) - passes / total_students
            heapq.heappush(heap,(-gain,i))
        
        while extra:
            max_gain,index = heapq.heappop(heap)
            classes[index][0]+=1
            classes[index][1]+=1
            passes = classes[index][0]
            total_students = classes[index][1]
            gain = (passes+1) / (total_students+1) - passes / total_students
            heapq.heappush(heap,(-gain,index))
            extra-=1
        #print(classes)
        avg = 0
        for i in range(n):
            avg+= classes[i][0]/classes[i][1]
        
        return avg/n
 
            
