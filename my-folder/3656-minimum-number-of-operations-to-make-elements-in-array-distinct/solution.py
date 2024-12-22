class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        operations = 0
        n = len(nums)
        for i in range(n):
            count = Counter(nums)
            correct = False
            for key,val in count.items():
                if val>=2:
                    correct = True
                    break
            if correct:
                if len(nums)>=3:
                    for i in range(3):
                        nums.pop(0)
                    operations+=1
                else:
                    operations+=1
                    while nums:
                        nums.pop(0)
        return operations
