class Solution:
    def lexSmallestNegatedPerm(self, n: int, target: int) -> List[int]:
        s =  ( n*(n+1) ) // 2
        if abs(target) > s:
            return []
        if ( s - target ) %2 != 0:
            return []
        
        diff = s - target
        #print(f'diff: {diff}')
        
        ans = set()
        x = n
        while diff:
            if 2*x <= diff:
                ans.add(x)
                diff-=2*x
            x-=1
        output = []
        for i in range(1,n+1):
            if i in ans:
                output.append(-i)
            else:
                output.append(i)
        return sorted(output)

