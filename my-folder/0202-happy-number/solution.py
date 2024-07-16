class Solution:
    def isHappy(self, n: int) -> bool:

        def getSum(num):
            total = 0

            while num:
                digit = num%10
                total+= digit*digit
                num = (num//10)
            return total


        slow = n
        fast = n

        while True:
            slow = getSum(slow)
            fast = getSum(getSum(fast))

            if fast==slow:
                break
        return slow==1
        

        




        
