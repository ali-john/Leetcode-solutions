class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        table = {'2':['a','b','c'],'3':['d','e','f'],
        '4':['g','h','i'], '5':['j','k','l'], '6':['m','n','o'],
        '7':['p','q','r','s'], '8':['t','u','v'], '9':['w','x','y','z']
        }

        n = len(digits)
        ans = []
        def generate(index, comb):
            if index == n:
                ans.append(comb)
                return
            letter = digits[index]
            for char in table[letter]:
                generate(index+1, comb+char)
        
        generate(0,'')
        return ans
