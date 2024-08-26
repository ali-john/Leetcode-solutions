class Solution:
    def discountPrices(self, sentence: str, discount: int) -> str:
        s = sentence.split(" ")
        def check(st):
            st = st[1:]
            if len(st)<1:
                return False
            for char in st:
                if not char.isdigit():
                    return False
            return True

        for i in range(len(s)):
            if s[i][0]=='$':
                if check(s[i]):
                    num = int(s[i][1:])
                    num = num - num*(discount/100)
                    num = "%.2f" % num
                    s[i] = '$'+str(num)
        
        
        return " ".join(s)
