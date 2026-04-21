class Solution:
    def maximumXor(self, s: str, t: str) -> str:
        c = Counter(t)
        ans = []
        for i in range(len(s)):
            if s[i] == '0':
                if c['1']:
                    ans.append('1')
                    c['1']-=1
                    if c['1'] == 0:
                        del c['1']
                else:
                    ans.append('0')
                    c['0']-=1
                    if c['0'] == 0:
                        del c['0']
            else:
                if c['0']:
                    ans.append('1')
                    c['0']-=1
                    if c['0'] == 0:
                        del c['0']
                else:
                    ans.append('0')
                    c['1']-=1
                    if c['1'] == 0:
                        del c['1']
        return "".join(ans)
            
