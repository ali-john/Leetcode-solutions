class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        table = {'2':['a','b','c'],'3':['d','e','f'],
        '4':['g','h','i'], '5':['j','k','l'], '6':['m','n','o'],
        '7':['p','q','r','s'], '8':['t','u','v'], '9':['w','x','y','z']
        }
        if len(digits)==0:
            return []
        output = []
        def backtrack(index,combination):
            if index==len(digits):
                output.append(combination)
                return

            keys = table.get(digits[index])
            for key in keys:
                backtrack(index+1,combination+key)
            
        backtrack(0,'')
        return output


            

            
        







        
