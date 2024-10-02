class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        temp = sorted(arr)
        table = {}
        rank = 1
        for i,num in enumerate(temp):
            if table.get(num) is None:
                table[num] = rank
                rank+=1

        output = [0]*len(arr)
        for i,num in enumerate(arr):
            output[i] = table[num]
        return output
