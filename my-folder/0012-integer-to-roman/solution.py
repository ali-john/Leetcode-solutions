class Solution:
    def intToRoman(self, num: int) -> str:
        output = []
        ones = num%10
        tens = num%100 - ones
        hundered = num%1000 - tens - ones
        thousand = (num - (ones+tens+hundered))//1000
        
        #print(f'{thousand}: {hundered}: {tens}: {ones}')
        # process thousands:
        if thousand!=0:
            output.append('M'*thousand)
        if hundered!=0:
            if hundered==400: output.append('CD')
            elif hundered==900: output.append('CM')
            elif hundered==500: output.append('D')
            elif hundered==1000:output.append('M')
            elif hundered>500:
                times = (hundered-500)//100
                output.append('D')
                output.append('C'*times)
            elif hundered<500: 
                times = hundered//100
                output.append('C'*times)
        if tens!=0:
            if tens ==50: output.append('L')
            elif tens == 40: output.append('XL')
            elif tens == 90: output.append('XC')
            elif tens==100: output.append('C')
            elif tens>50:
                times = (tens - 50)//10
                output.append('L')
                output.append('X'*times)
            elif tens<50:
                times = tens//10
                output.append('X'*times)
        if ones!=0:
            if ones==1: output.append('I')
            elif ones==5: output.append('V')
            elif ones==4: output.append('IV')
            elif ones==9: output.append("IX")
            elif ones<5:
                output.append("I"*ones)
            elif ones>5:
                output.append("V")
                times = ones - 5
                output.append("I"*times)
        print(output)
        return ''.join(output)


