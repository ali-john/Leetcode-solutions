class Solution:
    def maximumGroups(self, grades: List[int]) -> int:
        n = len(grades)
        grades = sorted(grades)

        used = 0
        k = 0
        while used + (k + 1) <= n:
            k+=1
            used+=k
        return k
        
        # i = 0
        # group_sum = []
        # group_count = 1
        # while i + group_count <= n:
        #     curr_sum = 0
        #     for _ in range(group_count):
        #         curr_sum+= grades[i]
        #         i+=1
        #     group_sum.append(curr_sum)
        #     group_count+=1
        # return len(group_sum)
        
       


    





