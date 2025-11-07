class Solution:
    def mostFrequentPrime(self, mat: List[List[int]]) -> int:
        rows = len(mat)
        cols = len(mat[0])
        primes = defaultdict(int)


        def is_prime(num):
            if num <= 1:
                return False
            i = 2
            while i*i <= num:
                if num%i == 0: return False
                i+=1
            return True
        
        directions = [(1,0),(-1,0), (0,1),(0,-1),(1,1),(-1,-1),(1,-1),(-1,1)]

        for i in range(rows):
            for j in range(cols):
                for dx, dy in product((1,-1,0), (1,-1,0)):
                    num = str( mat[i][j] )
                    if dx == 0 and dy == 0: continue
                    new_x = dx + i
                    new_y = dy + j
                    while 0 <= new_x < rows and 0 <= new_y < cols:
                        num+=str( mat[new_x][new_y] )
                        if  is_prime(int(num)):
                            primes[int(num)]+=1
                        new_x = dx + new_x
                        new_y = dy + new_y
        #print(primes)
        if not primes: return -1
        m = max(primes.values())
        # return the largest number with the highest frequency
        return int(max(int(x) for x in primes if primes[x] == m))





       
            


