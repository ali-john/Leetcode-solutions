class Solution:
    def nextBeautifulNumber(self, n: int) -> int:
        
        def is_balanced(num):
            counter = Counter(str(num))
            for key,value in counter.items():
                if int(key)!=value:
                    return False
            return True
        
        for i in range(n+1,10000000):
            if is_balanced(i):
                return i
        
