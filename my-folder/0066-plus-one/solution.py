class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        last = digits[len(digits)-1]
        if last!=9:
            digits[len(digits)-1]=last+1
            return digits
        else:
            string = ''.join(str(x) for x in digits)
            string = int(string) + 1
            string = str(string)
            output = [int(x) for x in string]
            return output


        
