class Solution:
    def minimizeResult(self, expression: str) -> str:
        table = defaultdict()
        ptr = 0
        while expression[ptr]!='+':
            ptr+=1
        
        l2 = len(expression) - ptr-1
        l1 = ptr
        ptr2 = ptr+1
        for i in range(ptr-1,-1,-1):
            first_num = expression[i:ptr]
            before_num = expression[0:i]
            for j in range(l2):
                second_num = expression[ptr2:j+ptr2+1]
                after_num = expression[j+ptr2+1:]
                exp = f'{before_num}({first_num}+{second_num}){after_num}'
                if before_num!='' and after_num!='':
                    exp = f'{before_num}({first_num}+{second_num}){after_num}'
                    ans = int(before_num)*(int(first_num) + int(second_num) ) * int(after_num)
                    table[exp]=ans

                elif before_num=='' and after_num!='':
                    exp = f'({first_num}+{second_num}){after_num}'
                    ans = (int(first_num) + int(second_num) ) * int(after_num)
                    table[exp]=ans
                elif before_num!='' and after_num=='':
                    exp = f'{before_num}({first_num}+{second_num})'
                    ans = int(before_num)*(int(first_num) + int(second_num) )
                    table[exp]=ans
                else:
                    exp = f'({first_num}+{second_num})'
                    ans = (int(first_num) + int(second_num) )
                    table[exp]=ans

        min_val = min(table.values())
        for key,val in table.items():
            if val==min_val:
                return key
