class Solution:
    def reformatNumber(self, number: str) -> str:
        digits = []

        for char in number:
            if char.isdigit():
                digits.append(char)
        output = []
        while len(digits)>4:
            digit = digits[0:3]
            digit.append("-")
            output.append(digit)
            digits = digits[3:]
        
        if len(digits)==2:
            output.append(digits)
        elif len(digits)==3:
            output.append(digits)
        elif len(digits)==4:
            str1 = digits[0:2]
            str1.append("-")
            output.append(str1)
            output.append(digits[2:])
        

        final_output = ""
        for i in output:
            string = ''.join(i)
            final_output+=string
        return final_output

        




