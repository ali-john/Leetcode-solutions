class Solution:
    def minSwaps(self, s: str) -> int:
        def find_diff(start):
            diff = 0
            for c in s:
                if c != start:
                    diff+=1
                start = '1' if start == '0' else '0'
            return diff // 2
        
        c = Counter(s)
        oneCount = c['1']
        zeroCount = c['0']
        if abs(oneCount - zeroCount) > 1:
            return -1
        
        if zeroCount > oneCount:
            return find_diff('0')
        if oneCount > zeroCount:
            return find_diff('1')
        return min(find_diff('0'), find_diff('1'))
    
        
        

        

