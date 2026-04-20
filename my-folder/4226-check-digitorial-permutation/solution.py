class Solution:
    def isDigitorialPermutation(self, n: int) -> bool:
        fact = {0:1, 1:1,2:2,3:6, 4:24, 5:120, 6:720, 7:5040, 8: 40320, 9:362880}
        n_copy = n
        s = 0
        while n_copy:
            digit = n_copy % 10
            n_copy //= 10
            s+=fact[digit]
        return Counter(str(s)) == Counter(str(n))

