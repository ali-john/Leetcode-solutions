class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        def get_waviness(num):
            num = str(num)
            if len(num) < 3: return 0
            wave = 0
            for i in range(1, len(num) -1):
                if ( int( num[i] ) > int(num[i-1]) and int( num[i] ) > int(num[i+1]) ) or ( int( num[i] ) < int(num[i-1]) and int( num[i] ) < int(num[i+1])   ):
                    wave+=1
            return wave

        ans = 0
        for num in range(num1, num2+1):
            ans+=get_waviness(num)
        return ans
