class Solution:
    def findGoodIntegers(self, n: int) -> list[int]:
        ans = []
        mapper = defaultdict(int)
        for i in range(int( n ** (1/3 ) + 1)):
            for j in range(i+1):
                temp = i**3 + j**3
                if temp <= n:
                    mapper[temp]+=1
        for num, count in mapper.items():
            if count >=2:
                ans.append(num)
        return sorted(ans)

                    

