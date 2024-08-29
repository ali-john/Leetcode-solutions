class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        table = defaultdict()
        
        def compute(inp,table):
            result = []
            if table.get(inp) is not None:
                return table[inp]
            all_nums = True
            operators = ['+','-','*']
            for operator in operators:
                if operator in inp:
                    all_nums = False
            
            if all_nums:
                result.append(int(inp))
                
            
            else:
                for i in range(len(inp)):
                    if inp[i] in operators: # split string
                        left = compute(inp[0:i],table)
                        right = compute(inp[i+1:],table)

                        for j in range(len(left)):
                            part_one = left[j]
                            for k in range(len(right)):
                                part_two = right[k]
                                
                                if inp[i]=='+':
                                    result.append(part_one+part_two)
                                elif inp[i]=='-':
                                    result.append(part_one-part_two)
                                elif inp[i]=='*':
                                    result.append(part_one*part_two)


            table[inp] = result
            return result
        return compute(expression,table)






        
