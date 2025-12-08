class Solution:
    def completePrime(self, num: int) -> bool:
        
        def is_prime(n):
            if n <= 1:
                return False  
            if n <= 3:
                return True  
            if n % 2 == 0 or n % 3 == 0:
                return False 
        
            i = 5
            while i * i <= n:
                if n % i == 0 or n % (i + 2) == 0:
                    return False
                i += 6
            return True
        str_num = str(num)
        for i in range(len(str_num)):
            pref = str_num[0:i]
            suff = str_num[i:]
            if len(pref) > 0:
                if not is_prime(int(pref)):
                    return False
            if len(suff) > 0:
                if not is_prime(int(suff)):
                    return False
        return True
        
