class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:


        i = 0
        j = 0
        if len(firstList)==0 or len(secondList)==0:
            return []

        result = []

        def overlap(i,j):
            firstOver = firstList[i][0]>=secondList[j][0] and firstList[i][0]<=secondList[j][1]
            secondOver = secondList[j][0]>=firstList[i][0] and secondList[j][0]<=firstList[i][1]

            return firstOver or secondOver

        while i<len(firstList) and j<len(secondList):
            if overlap(i,j):
                start = max(firstList[i][0], secondList[j][0])
                end = min(firstList[i][1],secondList[j][1])
                result.append([start,end])

            if firstList[i][1]<secondList[j][1]:
                i+=1
            else:
                j+=1
        
        return result
        




            







        
