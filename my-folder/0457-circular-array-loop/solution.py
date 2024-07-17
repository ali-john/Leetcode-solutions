class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        
        n = len(nums)

        def next_index(i):
            return (i+nums[i])%n

        for i in range(len(nums)):

            if nums[i]==0:
                continue
            

            slow = i
            fast = next_index(i)

            while nums[slow]*nums[fast]>0 and nums[slow]*nums[next_index(fast)]>0:

                if slow==fast:
                    if slow==next_index(slow): # check self -loop
                        break
                    return True
                
                slow = next_index(slow)
                fast = next_index(next_index(fast))
            

            slow = i
            while nums[slow] * nums[i] > 0:
                nums[slow] = 0
                slow = next_index(slow)
        
        return False


            



            


                    

