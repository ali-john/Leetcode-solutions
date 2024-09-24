class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        n = len(customers)
        
        without_power = 0
        for i, num in enumerate(grumpy):
            if num==0:
               without_power+= customers[i]
        
        extra_satisfied = 0
        for i in range(minutes):
            if grumpy[i]==1:
                extra_satisfied+=customers[i] # add customers that are satisfied with power

        max_extra_satisfied = extra_satisfied
        
        # now check for window to maximize max_extra_Satisfied
        start = 0
        for i in range(1,n-minutes+1):
            if grumpy[start]==1:
                extra_satisfied-=customers[start]
            if grumpy[i+minutes-1]==1:
                extra_satisfied+=customers[i+minutes-1]
            
            max_extra_satisfied = max(max_extra_satisfied,extra_satisfied)
            start+=1
        
        return without_power+max_extra_satisfied





